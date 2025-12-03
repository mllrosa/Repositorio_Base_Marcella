import flet as ft

def main(page: ft.Page):
    page.title = "Conversão de Moeda"
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E1E"
    page.window.width = 550
    page.window.height = 370
    page.window.max_width = 550
    page.window.max_height = 370

    # Taxa de câmbio fixa para a conversão
    taxa_cambio = 5.30

    # Variável para controlar a direção da conversão
    modo_conversao = ft.Ref()  # Vai armazenar a escolha do usuário

    # Função para cálculo de conversão
    def conversao_moeda(a):
        try:
            valor = float(imput_valor.value)  # Converte o valor para float

            # Verifica qual a direção da conversão escolhida pelo usuário
            if modo_conversao.current == "Dólar para Real":
                resultado = valor * taxa_cambio  # Conversão de USD para BRL
                page.open(ft.SnackBar(ft.Text(f"US${valor:.2f} = R${resultado:.2f}", color="white"), bgcolor="black"))
            elif modo_conversao.current == "Real para Dólar":
                resultado = valor / taxa_cambio  # Conversão de BRL para USD
                page.open(ft.SnackBar(ft.Text(f"R${valor:.2f} = US${resultado:.2f}", color="white"), bgcolor="black"))
            else:
                # Se nenhuma opção estiver selecionada
                page.open(ft.SnackBar(ft.Text("Selecione a direção da conversão!", color="white"), bgcolor="black"))
                
        except ValueError:
            # Exibe Snackbar com mensagem de erro
            page.open(ft.SnackBar(ft.Text("Por favor, insira um valor numérico válido.", color="white"), bgcolor="black"))
            imput_valor.value = ""

        page.update()

    # Campos e botões
    texto1 = ft.Text("Conversão de Moeda", size=25, color="white")
    imput_valor = ft.TextField(label="Digite o valor...", keyboard_type=ft.KeyboardType.NUMBER)
    
    # Adicionando o SegmentedButton para escolher a direção da conversão
    segment_button = ft.SegmentedButton(
        on_change=lambda e: modo_conversao.set(e.control.selected),
        content=[
            ft.SegmentedButton("Dólar para Real", value="Dólar para Real"),
            ft.SegmentedButton("Real para Dólar", value="Real para Dólar")
        ]
    )

    # Botão para fazer a conversão
    calcular_conversao = ft.ElevatedButton("CONVERTER", bgcolor="BLACK", color="WHITE", width=200, on_click=conversao_moeda)

    # Layout
    page.add(
        ft.Row("", alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row([texto1], alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row([segment_button], alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row([imput_valor], alignment="center"),
        ft.Row([calcular_conversao], alignment="center")
    )

ft.app(target=main)
