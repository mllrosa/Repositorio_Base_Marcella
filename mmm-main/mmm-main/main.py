import os
import flet as ft

def main(page: ft.Page):
    page.title = "AA"
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E1E"
    page.window.width = 550
    page.window.height = 390
    page.window.max_width = 550
    page.window.max_height = 390
    page.window.min_width = 550
    page.window.min_height = 390
    page.window.center()


    # Função para criar pastas
    def criar_pasta(e):
        global pasta
        pasta = imput1.value
        try:
            os.mkdir(pasta)
            informativo.value = f"Pasta criada: '{pasta}'"
        except FileExistsError:
            informativo.value = f"A pasta '{pasta}' já existe."
        page.update()
        
   
    # Função para criar arquivos
    def criar_arquivo(e):
        texto = imput1.value
        try:
            open(f"{pasta}\{imput1.value}", "w").close()
            informativo.value = f"Arquivo criado: '{texto}'"
        except Exception as erro:
            informativo.value = "adicionar um texto"
    
    
    def criar_arquivo(e):
        texto = imput1.value
        with open(f"{pasta}\{texto}", "w") as arq:
                arq.write("Conteúdo gerado por Python\n")
                informativo.value = f"{texto} criado com sucesso!"
    
    def deletar_arquivo(e):
        os.rmdir(imput1.value)
        
    def listar_arquivos():
        arquivos = os.listdir("SANTANA")
        for item in arquivos:
            informativo.value = item
            print(item)
   

    def renomear_arquivo(e):
        os.rename(imput1.value, imput2.value)
    
    page.update()

    # Campos e botões
    texto1 = ft.Text("PROJETO MULTIFUNÇÕES", size=25, color="white" )
    imput1 = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    imput2 = ft.TextField(label="Escreva o nome do arquivo/pasta...")



    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="BLACK", color="WHITE", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="BLACK", color="WHITE", width=200, on_click=criar_arquivo)
    botao_apagar = ft.ElevatedButton("EXCLUIR ARQUIVOS", bgcolor="BLACK", color="WHITE", width=200, on_click= deletar_arquivo)
    botao_renomear = ft.ElevatedButton("RENOMEAR ARQUIVOS", bgcolor="BLACK", color="WHITE", width=200, on_click= renomear_arquivo)
    botao_listar_arquivos = ft.ElevatedButton("LISTAR ARQUIVOS", bgcolor="BLACK", color="WHITE", width=200, on_click= listar_arquivos)
    informativo = ft.Text("", size=15, color="white")

    # Layout
    page.add(
        ft.Row("", alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row([texto1], alignment="center"),
        ft.Row([imput1], alignment="center"),
        ft.Row([imput2], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo, ], alignment="center"),
        ft.Row([ botao_renomear, botao_listar_arquivos], alignment="center"),
        ft.Row([botao_apagar], alignment="center"),
        ft.Row([informativo], alignment="center")
    )


ft.app(target=main)
