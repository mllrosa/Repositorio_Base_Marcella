import flet as ft
import math
from typing import List, Tuple

# -----------------------
#  Layout colors (customize)
# -----------------------
COLOR_BG = "#0D120E"
COLOR_BTN = "#2F3A34"
COLOR_BTN_DARK = "#262E2A"
COLOR_BTN_GREEN = "#3A5F35"
COLOR_BTN_EQUAL = "#8AD6DF"
COLOR_TEXT = "#E8F1E7"

scientific_buttons = [
    ["√", "π", "^", "!"],
    ["Deg", "sin(", "cos(", "tan("],
    ["Inv", "e", "ln(", "log("],
]

normal_buttons = [
    ["AC", "(", ")", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="],
]

# -----------------------
#  Parser / Evaluator
# -----------------------
Token = Tuple[str, str]
FUNCTION_NAMES = {"sin", "cos", "tan", "ln", "log", "sqrt"}

precedence = {
    "!": (6, "left", "postfix"),
    "%": (6, "left", "postfix"),
    "^": (5, "right", "binary"),
    "*": (4, "left", "binary"),
    "/": (4, "left", "binary"),
    "+": (3, "left", "binary"),
    "-": (3, "left", "binary"),
}

# Variáveis globais que podem ser modificadas
use_degrees = True
inv_mode = False

def tokenize(expr: str) -> List[Token]:
    """Tokeniza a expressão e aplica regras de multiplicação implícita adequadas."""
    s = expr.replace(" ", "").replace(",", ".")
    i = 0
    raw = []
    
    while i < len(s):
        c = s[i]
        
        # Raiz quadrada (√) - precisa ser tratado primeiro
        if c == "√":
            # Verificar se há número imediatamente após
            j = i + 1
            if j < len(s) and (s[j].isdigit() or s[j] == "." or s[j] == "("):
                raw.append(("FUNC", "sqrt"))
                i = j
                continue
            else:
                raw.append(("FUNC", "sqrt"))
                i += 1
                continue
        
        # number
        if c.isdigit() or (c == "." and i+1 < len(s) and s[i+1].isdigit()):
            j = i
            dot_count = 0
            while j < len(s) and (s[j].isdigit() or s[j] == "."):
                if s[j] == ".":
                    dot_count += 1
                    if dot_count > 1:
                        break
                j += 1
            raw.append(("NUMBER", s[i:j]))
            i = j
            continue
        
        # names and pi
        if c.isalpha() or c == "π":
            j = i
            while j < len(s) and (s[j].isalpha() or s[j] == "π"):
                j += 1
            name = s[i:j]
            # Check if this is a function (remove trailing '(' if present)
            func_name = name.rstrip('(')
            if func_name.lower() in FUNCTION_NAMES:
                raw.append(("FUNC", func_name.lower()))
                # Skip '(' if present
                if j < len(s) and s[j] == '(':
                    j += 1
                i = j
                continue
            # Otherwise treat as constant
            raw.append(("NAME", name))
            i = j
            continue
        
        # parentheses
        if c in "()":
            raw.append(("PAREN", c))
            i += 1
            continue
        
        # operators and special
        if c in "+-*/^%!×÷−":
            if c == "×": c = "*"
            if c == "÷": c = "/"
            if c == "−": c = "-"
            if c in "%!":
                raw.append(("OP_POST", c))
                i += 1
                continue
            raw.append(("OP", c))
            i += 1
            continue
        
        # unknown -> skip
        i += 1

    # Insert implicit multiplication where appropriate
    out: List[Token] = []
    for k in range(len(raw)):
        out.append(raw[k])
        
        # Caso especial para função sqrt seguida de número sem parênteses
        if k < len(raw) - 1:
            t1, v1 = raw[k]
            t2, v2 = raw[k+1]
            
            # Se temos sqrt seguido de número, não inserir multiplicação
            if t1 == "FUNC" and v1 == "sqrt" and t2 == "NUMBER":
                continue
            
            # Cases where we need implicit multiplication:
            insert_mul = False
            
            if t1 == "NUMBER" and (t2 == "FUNC" or t2 == "NAME" or (t2 == "PAREN" and v2 == "(")):
                insert_mul = True
            elif t1 == "PAREN" and v1 == ")" and (t2 == "NUMBER" or t2 == "FUNC" or t2 == "NAME" or (t2 == "PAREN" and v2 == "(")):
                insert_mul = True
            elif t1 == "OP_POST" and (t2 == "NUMBER" or t2 == "FUNC" or t2 == "NAME"):
                insert_mul = True
            elif (t1 == "FUNC" or t1 == "NAME") and (t2 == "NUMBER" or (t2 == "PAREN" and v2 == "(")):
                # But not if it's a function call like sin(30) or sqrt(9)
                if not (t1 == "FUNC" and t2 == "PAREN" and v2 == "("):
                    insert_mul = True
            
            if insert_mul:
                out.append(("OP", "*"))
    
    return out

def to_rpn(tokens: List[Token]) -> List[Token]:
    output = []
    stack: List[Token] = []
    
    for tok in tokens:
        ttype, val = tok
        
        if ttype == "NUMBER":
            output.append(tok)
        elif ttype == "NAME":
            output.append(tok)
        elif ttype == "FUNC":
            stack.append(tok)
        elif ttype == "OP":
            op = val
            while (stack and stack[-1][0] == "OP" and 
                   stack[-1][1] in precedence and
                   ((precedence[op][2] == "binary" and precedence[op][0] <= precedence[stack[-1][1]][0]) or
                    (precedence[op][2] == "postfix"))):
                output.append(stack.pop())
            stack.append(tok)
        elif ttype == "OP_POST":
            output.append(("OP", val))
        elif ttype == "PAREN":
            if val == "(":
                stack.append(tok)
            else:  # val == ")"
                while stack and not (stack[-1][0] == "PAREN" and stack[-1][1] == "("):
                    output.append(stack.pop())
                if stack and stack[-1][0] == "PAREN" and stack[-1][1] == "(":
                    stack.pop()
                if stack and stack[-1][0] == "FUNC":
                    output.append(stack.pop())
    
    while stack:
        output.append(stack.pop())
    
    return output

def apply_postfix(op: str, a: float) -> float:
    if op == "!":
        if a < 0 or int(a) != a:
            raise ValueError("Invalid factorial")
        if a > 1000:
            raise ValueError("Number too large for factorial")
        return math.factorial(int(a))
    if op == "%":
        return a / 100.0
    raise ValueError("Unknown postfix")

def apply_binary(op: str, a: float, b: float) -> float:
    if op == "+": 
        return a + b
    if op == "-": 
        return a - b
    if op == "*": 
        return a * b
    if op == "/": 
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    if op == "^": 
        try:
            return a ** b
        except:
            raise ValueError("Invalid exponentiation")
    raise ValueError("Unknown binary op: " + op)

def eval_rpn(rpn: List[Token]) -> float:
    stack: List[float] = []
    
    for tok in rpn:
        ttype, val = tok
        
        if ttype == "NUMBER":
            stack.append(float(val))
        elif ttype == "NAME":
            if val.lower() in ("pi", "π"):
                stack.append(math.pi)
            elif val.lower() == "e":
                stack.append(math.e)
            else:
                raise ValueError(f"Unknown constant: {val}")
        elif ttype == "FUNC":
            if not stack:
                raise ValueError("Missing operand for function")
            a = stack.pop()
            
            if val == "sqrt":
                if a < 0:
                    raise ValueError("Square root of negative number")
                stack.append(math.sqrt(a))
            elif val == "ln":
                if a <= 0:
                    raise ValueError("Logarithm of non-positive number")
                stack.append(math.log(a))
            elif val == "log":
                if a <= 0:
                    raise ValueError("Logarithm of non-positive number")
                stack.append(math.log10(a))
            elif val in ("sin", "cos", "tan"):
                global use_degrees, inv_mode
                
                if inv_mode:
                    if val == "sin":
                        if a < -1 or a > 1:
                            raise ValueError("asin argument out of range")
                        res = math.asin(a)
                    elif val == "cos":
                        if a < -1 or a > 1:
                            raise ValueError("acos argument out of range")
                        res = math.acos(a)
                    else:
                        res = math.atan(a)
                    
                    if use_degrees:
                        res = math.degrees(res)
                    stack.append(res)
                else:
                    if use_degrees:
                        a_rad = math.radians(a)
                    else:
                        a_rad = a
                    
                    if val == "sin":
                        stack.append(math.sin(a_rad))
                    elif val == "cos":
                        stack.append(math.cos(a_rad))
                    else:
                        stack.append(math.tan(a_rad))
            else:
                raise ValueError(f"Unknown function: {val}")
        elif ttype == "OP":
            if val in ("!", "%"):
                if not stack:
                    raise ValueError("Missing operand for postfix operator")
                a = stack.pop()
                stack.append(apply_postfix(val, a))
            else:
                if len(stack) < 2:
                    raise ValueError("Missing operands for binary operator")
                b = stack.pop()
                a = stack.pop()
                stack.append(apply_binary(val, a, b))
        else:
            raise ValueError(f"Unknown token type: {ttype}")
    
    if len(stack) != 1:
        raise ValueError(f"Invalid expression - stack has {len(stack)} items: {stack}")
    
    return stack[0]

def solve_expression(expr: str) -> str:
    if expr.strip() == "":
        return ""
    try:
        tokens = tokenize(expr)
        rpn = to_rpn(tokens)
        val = eval_rpn(rpn)
        
        if abs(val) < 1e-12:
            val = 0
        
        if val == float('inf') or val == float('-inf'):
            return "Erro: Overflow"
        
        if abs(val - round(val)) < 1e-10:
            return str(int(round(val)))
        
        return f"{val:.10g}".rstrip('0').rstrip('.')
    except Exception as e:
        return "Erro"

# -----------------------
#  Flet UI
# -----------------------
def main(page: ft.Page):
    page.title = "Calculadora Avançada"
    page.bgcolor = COLOR_BG
    page.padding = 15
    page.horizontal_alignment = "center"
    page.vertical_alignment = "end"

    # Variáveis locais
    scientific_visible = False
    
    # Dicionário para armazenar referências aos botões trigonométricos
    trig_buttons = {}
    
    # Posição do cursor
    cursor_pos = 0

    # Status text (criado antes para poder ser usado em várias funções)
    status_text = ft.Text("", size=12, color="#9EEBAA")
    
    def update_status():
        global use_degrees, inv_mode
        status_text.value = f"Modo: {'Graus' if use_degrees else 'Radianos'} | Inv: {'ON' if inv_mode else 'OFF'}"
        if hasattr(status_text, '_page') and status_text._page:
            status_text.update()

    # Campo de entrada editável
    display = ft.TextField(
        value="",
        text_size=45,
        color=COLOR_TEXT,
        border_color="transparent",
        cursor_color="#9EEBAA",
        cursor_width=3,
        multiline=False,
        read_only=False,
        text_align=ft.TextAlign.RIGHT,
        expand=False,
        height=110,
    )

    def update_cursor_position(e=None):
        nonlocal cursor_pos
        if display.value:
            cursor_pos = len(display.value)
        else:
            cursor_pos = 0

    def insert_at_cursor(text: str):
        """Insere texto na posição atual do cursor"""
        nonlocal cursor_pos
        current = display.value
        if cursor_pos < 0:
            cursor_pos = 0
        if cursor_pos > len(current):
            cursor_pos = len(current)
        
        new_text = current[:cursor_pos] + text + current[cursor_pos:]
        display.value = new_text
        cursor_pos += len(text)
        display.focus()

    def move_cursor_left():
        """Move o cursor para a esquerda"""
        nonlocal cursor_pos
        if cursor_pos > 0:
            cursor_pos -= 1
            display.focus()

    def move_cursor_right():
        """Move o cursor para a direita"""
        nonlocal cursor_pos
        if cursor_pos < len(display.value):
            cursor_pos += 1
            display.focus()

    # Atualizar os handlers do display
    def on_display_change(e):
        update_cursor_position()
    
    def on_display_focus(e):
        update_cursor_position()
    
    display.on_change = on_display_change
    display.on_focus = on_display_focus

    def press(e):
        nonlocal scientific_visible, cursor_pos
        
        t = e.control.data
        
        if t == "AC":
            display.value = ""
            cursor_pos = 0
        elif t == "⌫":
            current = display.value
            if current and cursor_pos > 0:
                new_text = current[:cursor_pos-1] + current[cursor_pos:]
                display.value = new_text
                cursor_pos -= 1
                display.focus()
        elif t == "=":
            result = solve_expression(display.value)
            display.value = result
            cursor_pos = len(result)
        elif t == "Deg":
            global use_degrees
            use_degrees = not use_degrees
            e.control.content = ft.Text("Rad" if not use_degrees else "Deg", 
                                       size=18, color=COLOR_TEXT)
            e.control.update()
            update_status()
        elif t == "Inv":
            global inv_mode
            inv_mode = not inv_mode
            # Atualizar botões trigonométricos
            update_trig_buttons()
            update_status()
        elif t in ["←", "→"]:
            if t == "←":
                move_cursor_left()
            else:
                move_cursor_right()
        else:
            insert_at_cursor(t)
        
        display.update()

    def update_trig_buttons():
        """Atualiza os rótulos dos botões trigonométricos no modo Inv"""
        global inv_mode
        for btn_data, btn_ref in trig_buttons.items():
            if btn_data in ["sin(", "cos(", "tan("]:
                if inv_mode:
                    new_text = f"{btn_data[:-1]}⁻¹("
                else:
                    new_text = btn_data
                btn_ref.data = new_text.replace('(', '')
                btn_ref.content = ft.Text(new_text, size=18, color=COLOR_TEXT)
                btn_ref.update()

    def build_normal_buttons(shrink=False):
        size = 70 if not shrink else 58
        rows = []
        for row in normal_buttons:
            row_controls = []
            for b in row:
                color = COLOR_BTN
                if b == "AC":
                    color = COLOR_BTN_GREEN
                elif b == "=":
                    color = COLOR_BTN_EQUAL
                elif b in ["(", ")"]:
                    color = COLOR_BTN_DARK
                
                btn = ft.Container(
                    data=b,
                    content=ft.Text(b, size=22 if not shrink else 18, color=COLOR_TEXT),
                    alignment=ft.alignment.center,
                    width=size,
                    height=size,
                    bgcolor=color,
                    border_radius=size,
                    on_click=press
                )
                row_controls.append(btn)
            rows.append(ft.Row(row_controls, alignment="center", spacing=10))
        return rows

    def build_scientific_buttons():
        rows = []
        for row in scientific_buttons:
            row_controls = []
            for b in row:
                if b == "Inv":
                    btn_text = "Inv⁻¹" if inv_mode else "Inv"
                    btn = ft.Container(
                        data=b,
                        content=ft.Text(btn_text, size=18, color=COLOR_TEXT),
                        alignment=ft.alignment.center,
                        width=65,
                        height=45,
                        bgcolor=COLOR_BTN_DARK if not inv_mode else "#4A3A35",
                        border_radius=16,
                        on_click=press
                    )
                elif b == "Deg":
                    global use_degrees
                    btn_text = "Rad" if not use_degrees else "Deg"
                    btn = ft.Container(
                        data=b,
                        content=ft.Text(btn_text, size=18, color=COLOR_TEXT),
                        alignment=ft.alignment.center,
                        width=65,
                        height=45,
                        bgcolor=COLOR_BTN_DARK,
                        border_radius=16,
                        on_click=press
                    )
                else:
                    func_base = b.rstrip('(')
                    if inv_mode and func_base in ["sin", "cos", "tan"]:
                        btn_text = f"{func_base}⁻¹("
                    else:
                        btn_text = b
                    
                    btn = ft.Container(
                        data=b,
                        content=ft.Text(btn_text, size=18, color=COLOR_TEXT),
                        alignment=ft.alignment.center,
                        width=65,
                        height=45,
                        bgcolor=COLOR_BTN_DARK,
                        border_radius=16,
                        on_click=press
                    )
                    if b in ["sin(", "cos(", "tan(", "ln(", "log("]:
                        trig_buttons[b] = btn
                row_controls.append(btn)
            rows.append(ft.Row(row_controls, alignment="center", spacing=8))
        return rows

    sci_box = ft.Column(build_scientific_buttons(), visible=False, spacing=6)
    normal_box = ft.Column(build_normal_buttons(), spacing=10)

    def toggle_scientific(e):
        nonlocal scientific_visible
        scientific_visible = not scientific_visible
        sci_box.visible = scientific_visible
        normal_box.controls = build_normal_buttons(shrink=scientific_visible)
        if scientific_visible:
            sci_box.controls = build_scientific_buttons()
        page.update()

    # Botões de navegação do cursor
    cursor_nav = ft.Row([
        ft.Container(
            data="←",
            content=ft.Text("←", size=20, color=COLOR_TEXT),
            alignment=ft.alignment.center,
            width=40,
            height=40,
            bgcolor=COLOR_BTN_DARK,
            border_radius=10,
            on_click=press
        ),
        ft.Container(
            data="→",
            content=ft.Text("→", size=20, color=COLOR_TEXT),
            alignment=ft.alignment.center,
            width=40,
            height=40,
            bgcolor=COLOR_BTN_DARK,
            border_radius=10,
            on_click=press
        ),
    ], alignment="center", spacing=10)
    
    expand_btn = ft.TextButton(
        "⇅ Científica", 
        on_click=toggle_scientific,
        style=ft.ButtonStyle(color=COLOR_TEXT)
    )

    title = ft.Text("Calculadora Avançada", size=24, color=COLOR_TEXT, weight="bold")
    
    display_container = ft.Container(
        content=display,
        bgcolor=COLOR_BTN_DARK,
        border_radius=20,
        padding=20,
        margin=ft.margin.only(bottom=10)
    )
    
    instructions = ft.Text(
        "Clique no display para mover o cursor • Use as setas para navegar",
        size=12,
        color="#888",
        text_align="center"
    )
    
    # Adicionar todos os componentes à página
    page.add(
        title,
        display_container,
        cursor_nav,
        status_text,
        expand_btn,
        sci_box,
        normal_box,
        instructions
    )
    
    # Atualizar status depois de adicionar à página
    update_status()
    
    # Focar no display inicialmente
    display.focus()

if __name__ == "__main__":
    ft.app(target=main)
    