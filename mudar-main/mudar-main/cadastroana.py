import flet as ft
import datetime
import re

def CadastroView(page: ft.Page):
    # Configuração da página
    page.title = "Criar conta - Fábrica do Programador"
    page.theme_mode = "dark"
    page.window.width = 500
    page.window.height = 800
    page.bgcolor = "#FFFFFF"

    state = {"step": 0}
    ano_atual = datetime.datetime.now().year
    ano_min = 1935
    ano_max = ano_atual - 5

    # Domínios permitidos de email
    email_dominios = [
        "@gmail.com", "@outlook.com", "@hotmail.com", "@yahoo.com", 
        "@aluno.santanadeparnaiba.sp.gov.br", "@edu.santanadeparnaiba.sp.gov.br"
    ]

    # Campos
    nome_field = ft.TextField(label="Nome completo", width=400)
    dia = ft.TextField(label="Dia", width=80, keyboard_type=ft.KeyboardType.NUMBER)
    mes = ft.Dropdown(
        label="Mês", width=150,
        options=[ft.dropdown.Option(m) for m in [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]]
    )
    ano = ft.TextField(label="Ano", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    
    genero = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="F", label="Feminino"),
            ft.Radio(value="M", label="Masculino"),
            ft.Radio(value="O", label="Outro"),
            ft.Radio(value="N", label="Prefiro não dizer"),
        ])
    )

    email = ft.TextField(label="E-mail", width=400)
    senha = ft.TextField(label="Senha", width=400, password=True, can_reveal_password=True)
    senha_conf = ft.TextField(label="Confirmar senha", width=400, password=True, can_reveal_password=True)
    telefone = ft.TextField(label="Telefone", width=400)

    # Máscara automática do telefone
    def formatar_telefone(e):
        valor = telefone.value.strip()
        numeros = "".join(filter(str.isdigit, valor))
        if len(numeros) > 11:
            numeros = numeros[:11]

        if len(numeros) >= 2:
            telefone.value = f"({numeros[:2]})"
            if len(numeros) >= 7:
                telefone.value += numeros[2:7]
                if len(numeros) > 7:
                    telefone.value += "-" + numeros[7:]
            else:
                telefone.value += numeros[2:]
        else:
            telefone.value = numeros
        telefone.update()

    telefone.on_change = formatar_telefone

    # Telas
    def tela_nome():
        return ft.Column(
            [
                ft.Text("Passo 1 de 5"),
                nome_field,
                ft.ElevatedButton("Próximo", on_click=avancar)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def tela_data_genero():
        return ft.Column(
            [
                ft.Text("Passo 2 de 5"),
                ft.Row([dia, mes, ano]),
                ft.Text("Gênero", weight="bold"),
                genero,
                ft.Row([
                    ft.TextButton("Voltar", on_click=voltar),
                    ft.ElevatedButton("Próximo", on_click=avancar)
                ])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def tela_email():
        return ft.Column(
            [
                ft.Text("Passo 3 de 5"),
                email,
                ft.Row([
                    ft.TextButton("Voltar", on_click=voltar),
                    ft.ElevatedButton("Próximo", on_click=avancar)
                ])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def tela_senha():
        return ft.Column(
            [
                ft.Text("Passo 4 de 5"),
                senha,
                senha_conf,
                ft.Row([
                    ft.TextButton("Voltar", on_click=voltar),
                    ft.ElevatedButton("Próximo", on_click=avancar)
                ])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def tela_telefone():
        return ft.Column(
            [
                ft.Text("Passo 5 de 5"),
                telefone,
                ft.Row([
                    ft.TextButton("Voltar", on_click=voltar),
                    ft.ElevatedButton("Criar conta", on_click=criar_conta)
                ])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    telas = [tela_nome, tela_data_genero, tela_email, tela_senha, tela_telefone]
    container = ft.Container(
        content=telas[0](),
        padding=20,
        alignment=ft.alignment.center
    )

    # Funções de navegação
    def avancar(e=None):
        # Validação do nome
        if state["step"] == 0:
            nome_digitado = nome_field.value.strip()
            if not nome_digitado or len(nome_digitado) < 10:
                mostrar_erro("Mínimo 10 caracteres!")
                return
            if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome_digitado):
                mostrar_erro("Use apenas letras!")
                return
            state["nome"] = nome_digitado

        # Data de nascimento e gênero
        elif state["step"] == 1:
            try:
                dia_int = int(dia.value)
                if not 1 <= dia_int <= 31:
                    mostrar_erro("Dia inválido!")
                    return
            except ValueError:
                mostrar_erro("Dia inválido!")
                return

            try:
                ano_int = int(ano.value)
                if ano_int < ano_min or ano_int > ano_max:
                    mostrar_erro(f"Ano deve ser entre {ano_min} e {ano_max}!")
                    return
            except ValueError:
                mostrar_erro("Ano inválido!")
                return

            if not genero.value:
                mostrar_erro("Informe seu gênero!")
                return

        # Email
        elif state["step"] == 2:
            if not any(email.value.lower().endswith(d) for d in email_dominios):
                mostrar_erro("Use um domínio permitido!")
                return

        # Senha
        elif state["step"] == 3:
            if len(senha.value) < 8:
                mostrar_erro("Mínimo 8 caracteres!")
                return
            if not re.search(r"[A-Z]", senha.value):
                mostrar_erro("Precisa ter letra maiúscula!")
                return
            if not re.search(r"[a-z]", senha.value):
                mostrar_erro("Precisa ter letra minúscula!")
                return
            if not re.search(r"\d", senha.value):
                mostrar_erro("Precisa ter número!")
                return
            if not re.search(r"\W", senha.value):
                mostrar_erro("Precisa ter símbolo!")
                return
            if senha.value != senha_conf.value:
                mostrar_erro("Senhas não coincidem!")
                return

        if state["step"] < len(telas) - 1:
            state["step"] += 1
            container.content = telas[state["step"]]()
            page.update()

    def voltar(e=None):
        if state["step"] > 0:
            state["step"] -= 1
            container.content = telas[state["step"]]()
            page.update()

    def mostrar_erro(mensagem):
        page.snack_bar = ft.SnackBar(ft.Text(mensagem), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    def criar_conta(e=None):
        # Revalidar senha
        if senha.value != senha_conf.value:
            mostrar_erro("Senhas não coincidem!")
            return

        # Revalidar telefone
        numeros = "".join(filter(str.isdigit, telefone.value))
        if len(numeros) != 11:
            mostrar_erro("Telefone deve ter 11 números!")
            return

        # Sucesso
        page.snack_bar = ft.SnackBar(ft.Text("Conta criada com sucesso!"), bgcolor="green")
        page.snack_bar.open = True
        page.update()

    # Layout final
    page.add(
        ft.Column(
            [container],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

    # Para executar, use esta linha FORA da função:
    ft.app(target=CadastroView)

print("Aplicação pronta! Execute com: ft.app(target=CadastroView)")