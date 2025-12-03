import os, flet as ft

# A ideia será vocês criarem uma interface que faça os comandos exigidos de um sistema simples com as bibliotecas mencionadas acima.
# 2 - Criar arquivos dentro da pasta e fora.

def main(page: ft.Page):
    page.title = "AA"
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E1E"
    page.window.width = 550
    page.window.height = 370
    page.window.max_width = 550
    page.window.max_height = 370

# FUNCOES ======================================================

    # 5 - Verificar e excluir arquivo FOI
    def verificar_excluir(a):
        texto = texto_principal.value
        try:
            if os.path.exists(texto):
                os.remove(texto)
                informativo.value = (f"Pasta {texto} deletada com sucesso")
            else:
                print("Arquivo não encontrado")
        except FileExistsError:
            informativo.value = f"A pasta '{texto}' não existe."
            

    # Função para verificar arquivos FOI
    def verificar_arquivos(a):
        arquivos = os.listdir()
        informativo.value = arquivos
        page.update()


    # 1 - Criar uma pasta
    # 2 - Criar arquivos dentro da pasta e fora.
    def criar_pasta(e):
        texto = texto_principal.value
        try:
            os.mkdir(texto)
            informativo.value = f"Pasta criada: '{texto}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto}' já existe."
        page.update()
    

    # Função para criar arquivos FOI
    def criar_arquivo(e):
        texto = texto_principal.value
        try:
            open(texto, "w").close()
            informativo.value = f"Arquivo criado: '{texto}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()


    def renomear_arquivos(a):
        try:
            texto_principal = ft.TextField(label="Escreva o novo nome do arquivo...")
            os.rename(texto_principal, texto_principal)
        except Exception as erro:
            informativo.value = "Digite os nomes corretamente!"
        page.update()

    # Campos e botões FOI
    texto1 = ft.Text("PROJETO MULTIFUNÇÕES", size=25, color="white" )
    texto_principal = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="BLACK", color="WHITE", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="BLACK", color="WHITE", width=200, on_click=criar_arquivo)
    botao_excluir_arquivo = ft.ElevatedButton("EXCLUIR ARQUIVOS", bgcolor="BLACK", color="WHITE", width=200, on_click= verificar_excluir)
    botao_renomear = ft.ElevatedButton("RENOMEAR ARQUIVOS", bgcolor="BLACK", color="WHITE", width=200, on_click= renomear_arquivos)
    botao_listar_arquivos = ft.ElevatedButton("LISTAR ARQUIVOS", bgcolor="BLACK", color="WHITE", width=200, on_click= verificar_arquivos)
    informativo = ft.Text("", size=15, color="white")

    
    

    # Layout
    page.add(
        ft.Row("", alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row([texto1], alignment="center"),
        ft.Row([texto_principal], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo, ], alignment="center"),
        ft.Row([ botao_renomear, botao_listar_arquivos], alignment="center"),
        ft.Row([botao_excluir_arquivo], alignment="center"),
        ft.Row([informativo], alignment="center")
    )

ft.app(target=main)