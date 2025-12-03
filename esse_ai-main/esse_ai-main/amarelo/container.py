import flet as ft

def main(page: ft.Page):
    expandido = ft.Ref[bool]()
    expandido.value = False

    titulo = ft.Text("Clique para expandir")
    container_ref = ft.Ref[ft.Container]()

    def toggle_expand(e):
        expandido.value = not expandido.value

        if expandido.value:
            container_ref.current.content = ft.Column([
                titulo,
                ft.Text("Conteúdo expandido aqui..."),
                ft.ElevatedButton("Ação extra")
            ])
            container_ref.current.padding = 15
            container_ref.current.bgcolor = "#f0f0f0"
            container_ref.current.border_radius = 10
            container_ref.current.elevation = 4  # 👈 sombra leve
        else:
            container_ref.current.content = ft.Row([
                titulo
            ])
            container_ref.current.padding = 5
            container_ref.current.bgcolor = None
            container_ref.current.border_radius = 0
            container_ref.current.elevation = 0  # remove sombra

        page.update()

    container = ft.Container(
        ref=container_ref,
        content=ft.Row([
            titulo
        ]),
        on_click=toggle_expand,
        padding=5,
        width=400,
        ink=True
    )

    page.add(container)

ft.app(target=main)
