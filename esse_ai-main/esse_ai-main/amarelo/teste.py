import flet as ft


def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.update()

    images = ft.Row(expand=1, wrap=False, scroll=ft.ScrollMode.ALWAYS)

    page.add( images)

    for i in range(0, 7):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=110,
                height=70,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

ft.app(target=main)
