
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

def Home(page: ft.Page):
    """Página principal do aplicativo"""
    
    # Configuração da página conforme solicitado
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

