import flet as ft
import matplotlib.pyplot as plt
import io
import base64  # Importar base64 do Python

def main(page: ft.Page):
    page.title = "Desempenho do Aluno"
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.bgcolor = "#121212"
    page.padding = 30

    # Gera o gráfico e o converte em imagem
    def gerar_grafico(tipo="geral"):
        fig, ax = plt.subplots(figsize=(5, 3))
        materias = ["Módulo 1", "Módulo 2", "Módulo 3"]
        notas = [80, 90, 70]
        frequencias = [92, 87, 95]

        if tipo == "geral":
            largura = 0.35
            x = range(len(materias))
            ax.bar([i - largura/2 for i in x], notas, width=largura, label="Notas", color="#FF7B00")
            ax.bar([i + largura/2 for i in x], frequencias, width=largura, label="Frequência", color="#00C853")
            ax.legend()
        elif tipo == "notas":
            ax.bar(materias, notas, color="#FF7B00")
            ax.set_title("Notas")
        elif tipo == "frequencia":
            ax.bar(materias, frequencias, color="#00C853")
            ax.set_title("Frequência")

        ax.set_ylim(0, 100)
        plt.tight_layout()

        # Converte o gráfico em imagem
        buf = io.BytesIO()
        plt.savefig(buf, format="png", transparent=True)
        plt.close(fig)
        buf.seek(0)
        # Usa o módulo base64 correto para converter
        img_base64 = base64.b64encode(buf.read()).decode()
        return ft.Image(src_base64=img_base64)

    grafico = ft.Container(content=gerar_grafico("geral"), alignment=ft.alignment.center)

    texto_legenda = ft.Column(
        [
            ft.Row([
                ft.Container(width=15, height=15, bgcolor="#FF7B00", border_radius=3),
                ft.Text("Notas", size=13, color="#CCCCCC")
            ], spacing=8),
            ft.Row([
                ft.Container(width=15, height=15, bgcolor="#00C853", border_radius=3),
                ft.Text("Frequência", size=13, color="#CCCCCC")
            ], spacing=8),
        ],
        spacing=6,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )

    def atualizar(tipo):
        grafico.content = gerar_grafico(tipo)
        page.update()

    botoes = ft.Row(
        [
            ft.ElevatedButton("Geral", on_click=lambda e: atualizar("geral"), bgcolor="#FF7B00", color="white"),
            ft.ElevatedButton("Notas", on_click=lambda e: atualizar("notas"), bgcolor="#FF7B00", color="white"),
            ft.ElevatedButton("Frequência", on_click=lambda e: atualizar("frequencia"), bgcolor="#FF7B00", color="white"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    page.add(
        ft.Column(
            [
                ft.Text("Desempenho", size=22, weight=ft.FontWeight.BOLD, color="#FF7B00"),
                grafico,
                texto_legenda,
                botoes,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
