import flet as ft

def main(page: ft.Page):
    page.title = "Boletim"
    page.bgcolor = "#FFFFFF"


    card_colegio = ft.ResponsiveRow([
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Instituição / Turma", size=14, 
                    text_align=ft.TextAlign.LEFT,
                    color="#333333"),
                    
                    ft.Text(
                        "FABRICA DE PROGRAMADORES\nSALA 03 - 14h",
                        size=15,
                        weight=ft.FontWeight.W_500,
                        text_align=ft.TextAlign.LEFT
                    ),
                ],
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            ),
            bgcolor="#FFFFFF",
            border=ft.border.all(1, "#E0E0E0"),
            border_radius=8,
            padding=15,
            expand=True, 
        )
    ])


    card_situacao = ft.ResponsiveRow(
    [
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Situação", size=14, color="#333333"),
                    ft.Text("Cursando", size=16, weight=ft.FontWeight.BOLD),
                ],
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
            ),
            bgcolor="#FFFFFF",
            border=ft.border.all(1, "#E0E0E0"),
            border_radius=8,
            padding=15,
            expand=True,
            alignment=ft.alignment.center, 
        )
    ]
    )

    ocorrencias = []  # lista de ocorrências (vazia = nenhuma)

    texto_ocorrencia = (
        ft.Text("Nenhuma ocorrência registrada", color="#888888", size=14)
        if not ocorrencias
        else ft.Column([ft.Text(o, size=14) for o in ocorrencias])
    )

    card_ocorrencias = ft.Container(
    content=ft.Column(
        [
            ft.Text("Ocorrências", size=14, color="#333333"),
            texto_ocorrencia,
        ],
        spacing=6,
    ),
    bgcolor="#FFFFFF",
    border=ft.border.all(1, "#E0E0E0"),
    border_radius=8,
    expand=True,  # faz o container expandir
    padding=15,
    )

    ocorenrias_card = ft.Row(
        controls=[card_ocorrencias],
        expand=True,  # deixa o row expandir na tela
    )


    topo = ft.Column(
            [
                card_colegio,
                ft.Container(height=10),
                card_situacao,
                ft.Container(height=10),
                ocorenrias_card
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
   
    page.add(
        topo
    )

ft.app(target=main)

