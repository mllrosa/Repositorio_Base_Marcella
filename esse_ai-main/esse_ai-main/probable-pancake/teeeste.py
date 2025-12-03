
import flet as ft
import time
import threading

def self(page: ft.Page):
    # Imagens do carrossel
    self.imagens_carrossel = [
        "img\\fabrica.jpg",
        "img\\premio.jpg",
        "img\\programa.jpg",
        "img\\santana.jpg"
    ]

    # Estados do carrossel
    self.indice_carrossel = 0
    self.carrossel_auto_ativo = True

    def criar_carrossel(self, funcao_proxima_imagem, funcao_imagem_anterior):
        """Cria o carrossel de imagens"""
    
    imagem_carrossel = ft.Image(
        src=self.imagens_carrossel[0],
        width=400, 
        height=200, 
        fit=ft.ImageFit.COVER, 
        border_radius=15
    )
    
    def atualizar_carrossel():
        imagem_carrossel.src = self.imagens_carrossel[self.indice_carrossel]

    container_carrossel = ft.Container(
        content=ft.Stack([
            imagem_carrossel,
            # Botão imagem anterior
            ft.Container(
                content=ft.IconButton(
                    icon="ARROW_BACK_IOS_NEW", 
                    icon_color="#ededed",
                    style=ft.ButtonStyle(bgcolor={"": ft.Colors.BLACK54})
                ), 
                alignment=ft.alignment.center_left
            ),
            # Botão próxima imagem
            ft.Container(
                content=ft.IconButton(
                    icon="ARROW_FORWARD_IOS", 
                    icon_color="#efefef",
                    style=ft.ButtonStyle(bgcolor={"": ft.Colors.BLACK54})
                ), 
                alignment=ft.alignment.center_right
            ),
        ]), 
        width=400, 
        height=200, 
        margin=10, 
        border_radius=15
    )
    return container_carrossel, atualizar_carrossel

    def get_view(self, pagina: ft.Page):
        """Retorna a view simplificada apenas com o carrossel"""
    
    # Funções do carrossel
    def proxima_imagem(e):
        self.indice_carrossel = (self.indice_carrossel + 1) % len(self.imagens_carrossel)
        atualizar_carrossel()
        pagina.update()

    def imagem_anterior(e):
        self.indice_carrossel = (self.indice_carrossel - 1) % len(self.imagens_carrossel)
        atualizar_carrossel()
        pagina.update()

    # Criar carrossel
    carrossel, atualizar_carrossel = self.criar_carrossel(proxima_imagem, imagem_anterior)

    # Layout final simplificado
    layout_final = ft.Container(
        content=ft.Column([
            ft.Text("Carrossel de Imagens", 
                    size=20, 
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER),
            carrossel
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20,
        expand=True
    )

    # Auto-play do carrossel
    def executar_auto_play():
        while self.carrossel_auto_ativo:
            time.sleep(3)
            if self.carrossel_auto_ativo and pagina is not None:
                self.indice_carrossel = (self.indice_carrossel + 1) % len(self.imagens_carrossel)
                atualizar_carrossel()
                try:
                    pagina.update()
                except:
                    self.carrossel_auto_ativo = False

    # Configuração da página
    pagina.title = "Carrossel Simples"
    pagina.window.width = 500
    pagina.window.height = 300
    
    # Iniciar thread do carrossel automático
    thread_auto_play = threading.Thread(target=executar_auto_play, daemon=True)
    thread_auto_play.start()

    return ft.View(
        route="/home",
        controls=[layout_final],
        vertical_alignment="center",
        horizontal_alignment="center",
    )