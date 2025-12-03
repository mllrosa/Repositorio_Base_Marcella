import flet as ft

def main(pagina: ft.Page):
    pagina.title = "APP"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def somar(a):
        caixa_texto.value= str(int(caixa_texto.value)+1)
        pagina.update()
    def diminuir(b):
        caixa_texto.value= str(int(caixa_texto.value)-1)
        pagina.update()

    # Criar os itens da pagina
    caixa_texto = ft.TextField(value=0, width=100, text_align=ft.TextAlign.CENTER)
    botao_menos = ft.IconButton(ft.Icons.REMOVE, on_click=diminuir)
    botao_mais = ft.IconButton(ft.Icons.ADD, on_click=somar)

    # Adicionar os itens na pagina
    pagina.add(
        ft.Row([botao_menos, caixa_texto, botao_mais], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main) #ft.app(target=main, view=ft.WEB_BROWSER) Para abrir no navegador e nao uma tela