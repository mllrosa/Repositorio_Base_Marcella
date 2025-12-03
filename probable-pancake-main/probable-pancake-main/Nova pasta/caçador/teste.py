import flet as ft

def main(page: ft.Page):
    page.title = "App Personalizado com Temas"

    # Tema claro
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE,
            on_primary=ft.Colors.WHITE,
            background=ft.Colors.WHITE,
            on_background=ft.Colors.BLACK,
        ),
        button_theme=ft.ButtonTheme(
            color_scheme=ft.ColorScheme(primary=ft.Colors.BLUE, on_primary=ft.Colors.WHITE)
        )
    )

    # Tema escuro
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.ORANGE,
            on_primary=ft.Colors.BLACK,
            background=ft.Colors.BLACK,
            on_background=ft.Colors.WHITE,
        ),
        button_theme=ft.ButtonTheme(
            color_scheme=ft.ColorScheme(primary=ft.Colors.ORANGE, on_primary=ft.Colors.BLACK)
        )
    )

    # Começa no modo claro
    page.theme_mode = ft.ThemeMode.LIGHT

    texto = ft.Text("Bem-vindo ao meu app!", size=22)
    botao = ft.ElevatedButton("Clique aqui")

    # Função para alternar tema
    def alternar_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            texto.value = "Modo Escuro Ativado"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            texto.value = "Modo Claro Ativado"
        page.update()

    toggle_btn = ft.OutlinedButton("Trocar Tema", on_click=alternar_tema)

    page.add(texto, botao, toggle_btn)

ft.app(target=main)
