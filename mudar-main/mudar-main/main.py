import flet as ft
def CadastroView(page:ft.Page):
    page.title = "Criar conta - Fábrica do Programador"
    page.theme_mode = "dark"
    page.window.width = 500
    page.window.min_width = 500
    page.window.max_width = 500
    page.window.height = 800
    page.window.min_height = 800
    page.window.max_height = 800



    # Configuração básica da página
    page.bgcolor = "#FFFFFF"
    page.title = "MENU APP"
    page.window.width = 500
    page.window.height = 900

    selected_index = 0

    # Funções principais
    def menu_item_clicked(e):
        nonlocal selected_index
        selected_index = e.control.data
        update_menu_style()

    def open_end_drawer(e):
        page.open(end_drawer)

    def update_menu_style():
        for i, item in enumerate(menu_items.controls):
            if i == selected_index:
                item.bgcolor = "#0A0DA1"
                item.content.controls[0].color = ft.Colors.WHITE
                item.content.controls[1].color = ft.Colors.WHITE
            else:
                item.bgcolor = ft.Colors.TRANSPARENT
                item.content.controls[0].color = "#666666"
                item.content.controls[1].color = "#666666"
        page.update()

    # Componentes do menu lateral
    end_drawer = ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        controls=[
            ft.NavigationDrawerDestination(
                label="SUPORTE",
                icon=ft.Icons.LIVE_HELP_ROUNDED,
            ),
            ft.NavigationDrawerDestination(
                label="CONFIGURAÇÕES",
                icon=ft.Icons.SETTINGS,
            ),
            ft.NavigationDrawerDestination(
                label="SAIR",
                icon=ft.Icons.EXIT_TO_APP,
            ),
        ],
    )

    # Menu inferior
    menu_items = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.HOME, size=28, color="#666666"),
                    ft.Text("Home", size=11, color="#666666")
                ], alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                padding=10, data=0, on_click=menu_item_clicked, width=70, height=65
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.NOTIFICATIONS, size=28, color="#666666"),
                    ft.Text("Notificações", size=11, color="#666666")
                ], alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                padding=10, data=1, on_click=menu_item_clicked, width=70, height=65
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.BOOK, size=28, color="#666666"),
                    ft.Text("Materiais", size=11, color="#666666")
                ], alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                padding=10, data=2, on_click=menu_item_clicked, width=70, height=65
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.TRENDING_UP, size=28, color="#666666"),
                    ft.Text("Desempenho", size=11, color="#666666")
                ], alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                padding=10, data=3, on_click=menu_item_clicked, width=70, height=65
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.PERSON, size=28, color="#666666"),
                    ft.Text("Perfil", size=11, color="#666666")
                ], alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                padding=10, data=4, on_click=menu_item_clicked, width=70, height=65
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    bottom_menu = ft.Container(
        content=menu_items,
        bgcolor="#EDEDED",
        padding=10,
        height=80
    )

    # Conteúdo principal
    header = ft.Container(
        content=ft.Row([
            ft.Text("FÁBRICA DE PROGRAMADORES", size=22, weight=ft.FontWeight.BOLD, color="#0A0DA1"),
            ft.IconButton(icon=ft.Icons.MENU, on_click=open_end_drawer),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        bgcolor="#E9E9E9",
        padding=20,
        height=80
    )

    content = ft.Container(
        content=ft.Column([
            ft.Text("Bem-vindo à Fábrica de Programadores!", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("Conteúdo principal aqui...", size=16, color="#2AC9A6"),
        ], scroll=ft.ScrollMode.ADAPTIVE),
        padding=15,
        expand=True
    )

    # Layout final
    page.add(
        ft.Stack([
            ft.Column([header, content], expand=True),
            ft.Container(content=bottom_menu, bottom=0, left=0, right=0)
        ], expand=True),
        end_drawer
    )
    

    ft.app(target=main)