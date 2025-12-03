import math
import flet as ft

def main(page: ft.Page):
    # Configuração do tema escuro
    page.title = "🧮 Calculadora Avançada"
    page.theme_mode = "dark"
    page.window.width = 470
    page.window.height = 700
    page.padding = 20
    page.bgcolor = "#1a1a1a"  # Preto escuro

    # Cores do tema
    CORES = {
        "fundo": "#1a1a1a",
        "card": "#2d2d2d",
        "card_claro": "#3d3d3d",
        "primario": "#1e3a8a",  # Azul escuro
        "primario_hover": "#2563eb",
        "texto_primario": "#ffffff",
        "texto_secundario": "#cccccc",
        "texto_resultado": "#60a5fa",
        "borda": "#404040",
        "perigo": "#dc2626"
    }

    entrada = ft.TextField(
        label="Digite a expressão",
        width=360,
        text_align="right",
        value="",
        bgcolor=CORES["card"],
        color=CORES["texto_primario"],
        border_color=CORES["borda"],
        focused_border_color=CORES["primario"],
        label_style=ft.TextStyle(color=CORES["texto_secundario"])
    )
    
    resultado = ft.Text(
        value="", 
        color=CORES["texto_resultado"], 
        size=20, 
        weight="bold"
    )

    def calcular(e):
        expressao = entrada.value.strip()

        if not expressao:
            resultado.value = "⚠️ Digite algo!"
            page.update()
            return

        try:
            # Operações científicas suportadas
            expressao = expressao.replace("^", "**")
            expressao = expressao.replace("√", "math.sqrt")

            # Permitir o uso de funções matemáticas
            permitido = {
                "math": math,
                "__builtins__": {},
            }

            valor = eval(expressao, permitido)
            resultado.value = f"= {valor}"
                
        except ZeroDivisionError:
            resultado.value = "❌ Erro: divisão por zero!"
        except Exception:
            resultado.value = "❌ Erro: expressão inválida!"
        page.update()

    def limpar(e):
        entrada.value = ""
        resultado.value = ""
        page.update()

    def obter_cor_botao(texto):
        if texto == "=":
            return CORES["primario"]
        elif texto == "C":
            return CORES["perigo"]
        elif texto in ["sin(", "cos(", "tan(", "log(", "√(", "^", "!"]:
            return CORES["card_claro"]
        else:
            return CORES["card"]
    
    def obter_cor_texto_botao(texto):
        if texto in ["=", "C"]:
            return CORES["texto_primario"]
        else:
            return CORES["texto_primario"]

    # Criação dos botões numéricos e de operações
    botoes = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["(", ")", "^", "√("],
        ["sin(", "cos(", "tan(", "log("],
        ["!", "C"],
    ]

    def clique(e):
        valor = e.control.text

        if valor == "=":
            calcular(e)
        elif valor == "C":
            limpar(e)
        elif valor == "!":
            try:
                num = float(entrada.value)
                entrada.value = str(math.factorial(int(num)))
            except:
                resultado.value = "❌ Erro no fatorial!"
            page.update()
        else:
            entrada.value += valor
            page.update()

    grid = ft.Column(spacing=8)
    for linha in botoes:
        row = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=b,
                    width=80,
                    height=50,
                    on_click=clique,
                    bgcolor=obter_cor_botao(b),
                    color=obter_cor_texto_botao(b),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        elevation=2,
                        overlay_color=CORES["primario_hover"] if b == "=" else "#4d4d4d"
                    )
                ) for b in linha
            ],
            alignment="center",
            spacing=8
        )
        grid.controls.append(row)

    # Container principal com fundo escuro
    container_principal = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column([
                        entrada,
                        resultado,
                    ]),
                    padding=15,
                    border_radius=10,
                    bgcolor=CORES["card"]
                ),
                ft.Divider(color=CORES["borda"], height=20),
                ft.Container(
                    content=grid,
                    padding=10,
                    border_radius=10,
                    bgcolor=CORES["card"]
                ),
            ],
            horizontal_alignment="center",
            alignment="center"
        ),
        padding=20,
        border_radius=15,
        bgcolor=CORES["fundo"]
    )

    page.add(container_principal)

ft.app(target=main)