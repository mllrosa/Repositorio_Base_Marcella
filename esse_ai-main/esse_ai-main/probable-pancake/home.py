import flet  as ft
from flet import *

def Home(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK 
    page.title = "MENU APP"
    page.window.width = 390
    page.window.height = 740
    page.window.max_width = 390
    page.window.max_height = 740
    page.window.min_width = 390
    page.window.min_height = 740

    # ===================================== CRIANDO FUCOES DOS ELEMENTOS
    # FUNCAO DO MENU
    def clicou_menu(e):
        item = e.control.text
        if item == "Suporte":
            print("Abrir suporte...")
        elif item == "Configurações":
            print("Abrir configurações...")
        elif item == "Tema":
            # Alternar entre claro e escuro
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
            else:
                page.theme_mode = ft.ThemeMode.DARK
            print(f"Tema alterado para: {page.theme_mode}")
            page.update()

    # FUNCAO PARA MUDAR DE TELA
    def mudar_tela(nova_tela):
        page.controls.clear()
        page.add(nova_tela)    
        page.update()     
    # ft.ElevatedButton("Voltar para Login",on_click=lambda _: mudar_tela(tela()))
    


    # ===================================== CRIANDO ELEMENTOS
    # Titulo da app/nome do app
    nome_da_tela = Text("NomeApp", size=18, weight=FontWeight.BOLD)

    # Botão de menu
    botao_menu_pequeno = ft.PopupMenuButton(icon="MORE_VERT", icon_size=30, items=[
            ft.PopupMenuItem(text="Suporte", icon="HELP_OUTLINE_ROUNDED", on_click=clicou_menu),
            ft.PopupMenuItem(text="Configurações", icon="SETTINGS_OUTLINED", on_click=clicou_menu),
            ft.PopupMenuItem(text="Tema", icon="WB_SUNNY_OUTLINED", on_click=clicou_menu),
        ],)
    
    # NavBar inferior (Home, Notificacoes, Desempenho, Perfil, )
    page.navigation_bar = NavigationBar(
        destinations = [
            NavigationBarDestination(icon=Icons.HOME_OUTLINED, label="Início"),
            NavigationBarDestination(icon=Icons.LIBRARY_BOOKS_OUTLINED, label="Desempenho"),
            NavigationBarDestination(icon=Icons.MESSAGE_OUTLINED, label="Notificações"),
            NavigationBarDestination(icon=Icons.TAG_FACES_OUTLINED, label="Perfil"),
        ]
    )

    # Container
    
    


    # ===================================== ALINHANDO ELEMENTOS
    # ------------------------------------- ALINHAMENTO DOS ELEMENTOS NA PAGINA

    topo = Row(
        controls=[nome_da_tela, botao_menu_pequeno],
        alignment=MainAxisAlignment.SPACE_BETWEEN
    )

    conteudo = Column(
        controls=[
            Container(
                content=topo,
                padding=10
            ),
            # Outros widgets podem ser adicionados aqui
        ],
        expand=True
    )


    # topo = ft.Row(
    #     controls=[botao_menu_pequeno],
    #     alignment=ft.MainAxisAlignment.END
    # )

    page.add( conteudo)

ft.app(target=Home)

# add um pouco sobre o perfil, nos proxismos dias..., um pouco sobre a fab
