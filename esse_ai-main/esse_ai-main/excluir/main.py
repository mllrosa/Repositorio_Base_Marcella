import flet  as ft
from flet import *
import webbrowser
import time
import threading

def Home(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.DARK 
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
    page.title = "MENU APP"
    page.window.width = 390
    page.window.height = 740
    page.window.max_width = 390
    page.window.max_height = 740
    page.window.min_width = 390
    page.window.min_height = 740
    page.scroll = "auto"

    # DAQUI PRA BAIXO É O NAVIGATIONBARR   =========================
    page.navigation_bar = NavigationBar( destinations = [
            NavigationBarDestination(icon=Icons.HOME_OUTLINED, label="Início"),
            NavigationBarDestination(icon=Icons.LIBRARY_BOOKS_OUTLINED, label="Desempenho"),
            NavigationBarDestination(icon=Icons.MESSAGE_OUTLINED, label="Notificações"),
            NavigationBarDestination(icon=Icons.TAG_FACES_OUTLINED, label="Perfil"),
        ]
    )

    # DTUDO SOBRE O AppBar =========================
    def clicou_menu(e):
        item = e.control.text
        if item == "Suporte":
            print("Abrir suporte...")
        elif item == "Configurações":
            print("Abrir configurações...")
        elif item == "Tema":
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
                page.theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
            else:
                page.theme_mode = ft.ThemeMode.DARK
                page.theme = ft.Theme(color_scheme_seed=ft.Colors.ORANGE)
            print(f"Tema alterado para: {page.theme_mode}")
        page.update()

    
    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("NomeApp"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.SHARE_ROUNDED),
            ft.PopupMenuButton(
                items=[
            ft.PopupMenuItem(text="Suporte", icon="HELP_OUTLINE_ROUNDED", on_click=clicou_menu),
            ft.PopupMenuItem(text="Configurações", icon="SETTINGS_OUTLINED", on_click=clicou_menu),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Tema", icon="WB_SUNNY_OUTLINED", on_click=clicou_menu),
                    
                ]
            ),
        ],
    )

    

    # # TUDO SOBRE O ICONE PERFIL =========================
    # page.padding = 15
    # perfil = ft.Row(
    #     spacing=15,
    #     controls=[
    #         ft.CircleAvatar(
    #             content=ft.Text("X", size=24, weight="bold", color=ft.Colors.WHITE),
    #             bgcolor=ft.Colors.GREEN,
    #             radius=30
    #         ),
    #         ft.Column(
    #             spacing=3,
    #             alignment="center",
    #             controls=[
    #                 ft.Text("Nome", size=18, weight="bold"),
    #                 ft.Row(
    #                     spacing=5,
    #                     controls=[
    #                         ft.Text("@nome.com", size=14),
    #                         ft.Text("•", size=14),
    #                         ft.Text("Ver perfil", size=14),
    #                         ft.Icon(ft.Icons.CHEVRON_RIGHT, size=16),
    #                     ] ) ] ) ] )
    # page.add(perfil)


    # # É O CARROSSEL  =========================
    # slides = [
    #     ft.Image("imagem_fabrica.png", width=500, height=300, fit=ft.ImageFit.COVER, border_radius=10),
    #     ft.Image("imagem_gabi.png", width=500, height=300, fit=ft.ImageFit.COVER, border_radius=10),
    #     ft.Image("imagem_laura.png", width=500, height=300, fit=ft.ImageFit.COVER, border_radius=10),
    # ]

    # # Índice atual
    # current_index = ft.Ref[int]()
    # current_index.value = 0

    # # Container onde o slide será mostrado
    # slide_view = ft.Container(content=slides[current_index.value], width=500, height=300, border_radius=10)

    # # Atualizar slide
    # def update_slide(index):
    #     slide_view.content = slides[index]
    #     for i, d in enumerate(dots.controls):
    #         d.bgcolor = "red" if i == index else "white"
    #     page.update()

    # # Botão próximo
    # def next_slide(e):
    #     current_index.value = (current_index.value + 1) % len(slides)
    #     update_slide(current_index.value)

    # # Botão anterior
    # def prev_slide(e):
    #     current_index.value = (current_index.value - 1) % len(slides)
    #     update_slide(current_index.value)

    # # Indicadores (bolinhas)
    # dots = ft.Row(
    #     controls=[
    #         ft.Container(width=15, height=5, bgcolor="white", border_radius=5)
    #         for _ in slides
    #     ],
    #     alignment="center",
    #     spacing=5,
    # )
    # dots.controls[0].bgcolor = "red"

    # # Botões estilizados como na imagem
    # prev_button = ft.IconButton(
    #     icon=ft.Icons.KEYBOARD_ARROW_LEFT_SHARP,
    #     icon_color="white",
        
    #     on_click=prev_slide,
    #     style=ft.ButtonStyle(shape=ft.CircleBorder())
    # )
    # next_button = ft.IconButton(
    #     icon_color="white",
    #     icon=ft.Icons.KEYBOARD_ARROW_RIGHT_ROUNDED,
        
    #     on_click=next_slide,
    #     style=ft.ButtonStyle(shape=ft.CircleBorder())
    # )

    # # Layout com botões sobrepostos ao slide
    # carousel = ft.Stack(
    #     controls=[
    #         slide_view,
    #         ft.Row([prev_button, ft.Container(expand=True), next_button],
    #                alignment="spaceBetween",
    #                width=500,
    #                height=300,
    #                vertical_alignment="center"),
    #     ],
    #     width=500,
    #     height=300,
    # )
    # page.add(carousel)

        
    primary_color = "#1E5FE9"
    secondary_color = "#2AC9A6"
    carousel_images = [
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400",
        "https://images.unsplash.com/photo-1555099962-4199c345e5dd?w=400",
        "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=400",
        "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=400"
    ]
    carousel_index = 0
    auto_play_enabled = True

    def create_profile_section(pick_file):
        """Seção de perfil do aplicativo"""
        return ft.Container(
            content=ft.Row([
                ft.Stack([
                    ft.Image(
                        src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=200",
                        width=110, height=110, fit=ft.ImageFit.COVER, border_radius=110
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            icon="CAMERA_ALT", icon_size=20, icon_color="white",
                            on_click=pick_file, tooltip="Adicionar Foto",
                            style=ft.ButtonStyle(bgcolor={"": primary_color}, shape=ft.CircleBorder())
                        ),
                        alignment=ft.alignment.bottom_right,
                    )
                ]),
                ft.Column([
                    ft.Text("Usuário", size=18, weight=ft.FontWeight.BOLD, color="#000000"),
                    ft.Text("Programador Iniciante", size=12, color="#000000"),
                    ft.ElevatedButton(
                        "Editar Perfil", icon="EDIT", height=30,
                        style=ft.ButtonStyle(bgcolor={"WHITE": secondary_color}, padding=10)
                    )
                ], spacing=3, expand=True)
            ], alignment=ft.MainAxisAlignment.START),
            padding=15, border_radius=15, margin=10
        )

    def create_carousel(next_image, previous_image):
        """Carrossel de imagens do aplicativo"""
        carousel_image = ft.Image(
            src=carousel_images[0],
            width=400, height=200, fit=ft.ImageFit.COVER, border_radius=15
        )
        
        def update_carousel():
            carousel_image.src = carousel_images[carousel_index]

        carousel = ft.Container(
            content=ft.Stack([
                carousel_image,
                ft.Container(
                    content=ft.IconButton(
                        icon="ARROW_BACK_IOS_NEW", icon_color="#ededed",
                        on_click=previous_image,
                        style=ft.ButtonStyle(bgcolor={"": ft.Colors.BLACK54})
                    ), alignment=ft.alignment.center_left
                ),
                ft.Container(
                    content=ft.IconButton(
                        icon="ARROW_FORWARD_IOS", icon_color="#efefef",
                        on_click=next_image,
                        style=ft.ButtonStyle(bgcolor={"": ft.Colors.BLACK54})
                    ), alignment=ft.alignment.center_right
                ),
            ]), width=400, height=200, margin=10, border_radius=15
        )
        
        return carousel, update_carousel

    def auto_play(page, update_carousel):
        """Função para rodar o carrossel automaticamente"""
        global carousel_index, auto_play_enabled
        
        def auto_play_thread():
            while auto_play_enabled:
                time.sleep(3)
                if auto_play_enabled and page is not None:
                    carousel_index = (carousel_index + 1) % len(carousel_images)
                    update_carousel()
                    try:
                        page.update()
                    except:
                        # Se a página foi fechada, para o loop
                        auto_play_enabled = False

        # Iniciar a thread do carrossel
        threading.Thread(target=auto_play_thread, daemon=True).start()
        
        # File Picker (botão de adicionar foto de perfil)
        file_picker = ft.FilePicker()
        page.overlay.append(file_picker)

        def pick_file(e):
            file_picker.pick_files(allow_multiple=False)

        # Funções do carrossel
        def next_image(e):
            global carousel_index
            carousel_index = (carousel_index + 1) % len(carousel_images)
            update_carousel()
            page.update()

        def previous_image(e):
            global carousel_index
            carousel_index = (carousel_index - 1) % len(carousel_images)
            update_carousel()
            page.update()

        # Criar componentes
        profile_section = create_profile_section(pick_file)
        carousel, update_carousel = create_carousel(next_image, previous_image)

        # Conteúdo principal da página
        content = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("Bem-vindo à Fábrica de Programadores!", size=18, 
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    profile_section,
                    carousel,
                ], scroll=ft.ScrollMode.ADAPTIVE, expand=True),
                padding=15, expand=True
            )
        ], expand=True)

    # Layout final
    page.add(content)

    # Iniciar carrossel automático
    auto_play(page, update_carousel)

    # TUDO DO CONTEINER ABRIVEL =========================
    eventos = ft.Column(
        spacing=20,
        controls=[
            ft.Row(
                spacing=10,
                controls=[
                            ft.Container(
                                content=ft.Column([
                                    ft.Text("Subtítulo em negrito", weight="bold"),
                                    ft.Text(
                                        "Aquii vai depender de onde o aluno esta matriculado, mas tambem pode ser geral. o status poderia ser aula normal ou conter somente as novidades:\n"
                                        "• Usar weight='bold' para negrito\n"
                                        "• size=12 para tamanho pequeno",
                                        size=12,
                                    )
                                ]),
                                padding=10,
                                border_radius=10
                            ),
                        ]
                    )
                ]
            )
        

    page.add(
        ft.ExpansionTile(
            title=ft.Text("HOJE NA FABRICA DE PROGRAMADORES", size=12, weight="bold"),
            subtitle=ft.Text("O que será que será?"),
            affinity=ft.TileAffinity.PLATFORM,
            maintain_state=True,
            controls=[eventos],
        )
    )



    # BOTAO GRANDE OU BOTAO CUPERTINOFILLED  =========================
    page.add(ft.ResponsiveRow([
        ft.CupertinoFilledButton(
            content=ft.Text("BOTAO", size=15, weight="bold"),
            height = 55,
            opacity_on_click=0.3,
            on_click=lambda e: print("CupertinoFilledButton"),
        ),
     ]))
    page.add(ft.Divider())
    


    # DAQUI PRA BAIXO SAO AS TRES BOLINHAS OU LINKS  =========================
    def abrir_link(e, url):
        webbrowser.open(url)

    links = ft.Column(
        spacing=10,
        controls=[
            ft.Text("Links dos DEVS ++s", size=18, weight="bold"),
            ft.Row(
                alignment="spaceEvenly",
                controls=[
                    ft.Column(
                        spacing = 0,
                        horizontal_alignment="center",
                        controls=[
                            ft.IconButton(icon=ft.Icons.CIRCLE, icon_size=73, on_click=lambda e: abrir_link(e, "https://youtube.com")),
                            ft.Text("Siteeeeeeeeeee", size=14)
                        ]
                    ),
                    ft.Column(
                        spacing = 0,
                        horizontal_alignment="center",
                        controls=[
                            ft.IconButton(icon=ft.Icons.CIRCLE, icon_size=73, on_click=lambda e: abrir_link(e, "https://youtube.com")),
                            ft.Text("Siteeeeeeeeeee", size=14)
                        ]
                    ),
                    ft.Column(
                        spacing = 0,
                        horizontal_alignment="center",
                        controls=[
                            ft.IconButton(icon=ft.Icons.CIRCLE, icon_size=73, on_click=lambda e: abrir_link(e, "https://youtube.com")),
                            ft.Text("Siteeeeeeeeeee", size=14)
                        ]
                    ),
                ]
            )
        ]
    )
    page.add(links)



    



    #================================================================
    # FUNCAO PARA MUDAR DE TELA para o navbar
    def mudar_tela(nova_tela):
        page.controls.clear()
        page.add(nova_tela)    
        page.update()     
    # ft.ElevatedButton("Voltar para Login",on_click=lambda _: mudar_tela(tela()))
    #================================================================

ft.app(target=Home)

