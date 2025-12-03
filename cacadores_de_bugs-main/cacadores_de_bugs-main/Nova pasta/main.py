import flet as ft
from flet import *


def DesempenhoView(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.DARK 
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_ORANGE)
    page.title = "PROGRAMADORES"
    page.window.width = 500
    page.window.height = 800
    page.window.max_width = 500
    page.window.max_height = 800
    page.window.min_width = 500
    page.window.min_height = 800
    page.scroll = 'auto'

    # ===================================== CRIANDO FUNÇÕES DOS ELEMENTOS
    def clicou_menu(e):
        item = e.control.text
        if item == "Suporte":
            print("Abrir suporte...")
        elif item == "Configurações":
            print("Abrir configurações...")
        elif item == "Tema":
            mudar_tema(None)

    def mudar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_ORANGE)
        print(f"Tema alterado para: {page.theme_mode}")
        page.update()

    # ===================================== CRIANDO ELEMENTOS
    appbar = ft.AppBar(
        leading_width=10,
        title=ft.Text("DESEMPENHO", weight="bold"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,  
        actions=[ 
                ft.IconButton(ft.Icons.HEARING, on_click=mudar_tema),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="TEMA", icon="WB_SUNNY_OUTLINED", on_click=mudar_tema),
                    ft.PopupMenuItem(text="CONFIGURAÇÕES", icon="SETTINGS_OUTLINED", on_click=clicou_menu),
                    ft.PopupMenuItem(text="SUPORTE", icon="HELP_OUTLINE_ROUNDED", on_click=clicou_menu),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="SAIR", icon="CLOSE_ROUNDED", on_click=clicou_menu),        
                ]
            ),
        ],
    )
     
    # Função para mudar de tela conforme índice do NavigationBar
    def mudar_tela(e):
        num = e.control.selected_index
        if num == 0:
            print("Indo para Início...")
        elif num == 1:
            print("Indo para Desempenho...")
        elif num == 2:
            print("Indo para Notificações...")
        elif num == 3:
            print("Indo para Perfil...")
        page.update()

    # Configurando o NavigationBar
    navbar = ft.NavigationBar(
        selected_index=1,  # Definindo como 1 para destacar a tela de Desempenho
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Início"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.BAR_CHART_OUTLINED,
                selected_icon=ft.Icons.BAR_CHART,
                label="Desempenho"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                selected_icon=ft.Icons.NOTIFICATIONS,
                label="Notificações"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON_OUTLINED,
                selected_icon=ft.Icons.PERSON,
                label="Perfil"
            ),
        ],
        on_change=mudar_tela
    )

    # Conteúdo principal da tela de Desempenho
    content = ft.Column(
        controls=[
            ft.Text("Tela de Desempenho", size=24, weight="bold"),
            ft.Text("Aqui você pode ver suas estatísticas e progresso."),
            # Adicione mais controles específicos da tela de desempenho aqui
        ],
        alignment="center",
        horizontal_alignment="center",
        expand=True
    )

    # REMOVA esta linha problemática:
    page.add(appbar, navbar)
    
    # return ft.View(
    #     route="/desempenho",
    #     controls=[
    #         appbar,
    #         content,  # Adicione o conteúdo aqui
    #         navbar
    #     ],
    #     vertical_alignment="center",
    #     horizontal_alignment="center"
    # )

ft.app(target=DesempenhoView)
