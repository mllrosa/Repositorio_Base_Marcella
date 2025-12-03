import os, flet as ft

# A ideia será vocês criarem uma interface que faça os comandos exigidos de um sistema simples com as bibliotecas mencionadas acima.
# 2 - Criar arquivos dentro da pasta e fora.

def main(page: ft.Page):
    page.title = "AA"
    page.theme_mode = "dark"
    page.bgcolor = "#5C0A0A"
    page.window.width = 550
    page.window.height = 430
    page.window.max_width = 550
    page.window.max_height = 430
    page.scroll='auto'

    texto_entrada = ft.ResponsiveRow(
        controls=[
            ft.TextField(
                label="Nome do arquivo ou pasta...",
                width=400,
                border_color="#D4AF37",
                label_style=ft.TextStyle(color="#5C0A0A"),
                cursor_color="#5C0A0A",
                color="#000000",
                bgcolor="#EAEAEA",
                col={"sm": 12, "md": 6},
            )
        ]
    )

    
    nome_antigo = ft.TextField(label="Nome atual", cursor_color= "#5C0A0A", label_style=ft.TextStyle(color="#5C0A0A"), width=190, border_color="#D4AF37", color="#000000", bgcolor="#EAEAEA")
    nome_novo = ft.TextField(label="Novo nome",cursor_color= "#5C0A0A", label_style=ft.TextStyle(color="#5C0A0A"), width=190, border_color="#D4AF37", color="#000000", bgcolor="#EAEAEA")
    informativo = ft.Text("", size=14, color="#D4AF37", italic=True)

    # Funções
    def criar_pasta(e):
        try:
            os.mkdir(texto_entrada.value)
            informativo.value = f"✅ Pasta criada: '{texto_entrada.value}'"
        except FileExistsError:
            informativo.value = f"⚠️ A pasta '{texto_entrada.value}' já existe."
        page.update()

    def criar_arquivo(e):
        try:
            open(texto_entrada.value, "w").close()
            informativo.value = f"✅ Arquivo criado: '{texto_entrada.value}'"
        except Exception as erro:
            informativo.value = f"❌ Erro: {erro}"
        page.update()

    def verificar_excluir(e):
        try:
            if os.path.exists(texto_entrada.value):
                os.remove(texto_entrada.value)
                informativo.value = f"🗑️ '{texto_entrada.value}' deletado com sucesso."
            else:
                informativo.value = f"⚠️ Arquivo não encontrado."
        except Exception as erro:
            informativo.value = f"❌ Erro: {erro}"
        page.update()

    def verificar_arquivos(e):
        arquivos = os.listdir()
        informativo.value = f"📂 Arquivos: {', '.join(arquivos)}"
        page.update()

    def renomear_arquivos(e):
        try:
            os.rename(nome_antigo.value, nome_novo.value)
            informativo.value = f"✏️ Renomeado para '{nome_novo.value}'"
        except Exception as erro:
            informativo.value = f"❌ Erro: {erro}"
        page.update()

    # Estilo dos botões
    def criar_botao(texto, icone, funcao):
        return ft.ElevatedButton(
            text=texto,
            icon=icone,
            on_click=funcao,
            style=ft.ButtonStyle(
                bgcolor="#5C0A0A",
                color="#D4AF37",
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=20,
                elevation=2,
            )
        )

    
    botoes = ft.Column([
        ft.Row([
            criar_botao("Criar Pasta", ft.Icons.FOLDER, criar_pasta),
            criar_botao("Criar Arquivo", ft.Icons.DESCRIPTION, criar_arquivo)
        ], alignment="center"),

        ft.Row([
            criar_botao("Excluir", ft.Icons.DELETE, verificar_excluir),
            criar_botao("Listar", ft.Icons.LIST, verificar_arquivos)
        ], alignment="center"),

        ft.Row([
            criar_botao("Renomear", ft.Icons.DRIVE_FILE_RENAME_OUTLINE, renomear_arquivos)
        ], alignment="center"),
        ft.ResponsiveRow([
            nome_antigo,
            nome_novo,
        ], alignment= 'center')
        
    ], spacing=10)

    # Título
    titulo = ft.Text("🛠️ Gerenciador de Arquivos", size=26, weight="bold", color="#D4AF37")

    # Container principal
    layout = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                texto_entrada,
                botoes,
                informativo
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        padding=25,
        bgcolor="#EAEAEA",  # fundo claro dentro do app
        border_radius=15,
        width=520
    )

    # Adicionar à página
    page.add(layout)

ft.app(target=main)
