import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora IMC"
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E1E"
    page.window.width = 550
    page.window.height = 370
    page.window.max_width = 550
    page.window.max_height = 370

    # Função para cálculo do IMC
    def calculo_imc(a):
        try:
            peso = float(imput_peso.value)  # Converte peso para float
            altura = float(imput_altura.value)  # Converte altura para float
            IMC = peso / (altura * altura)  # Fórmula para calcular IMC

            # Verifica a categoria do IMC
            if IMC < 18.5:
                text = "Abaixo do peso"
            elif 18.5 <= IMC < 24.9:
                text = "Peso normal"
            elif 24.9 <= IMC < 30:
                text = "Sobrepeso"
            else:
                text = "Obesidade"

            informativo = f"Seu IMC é: {IMC:.2f}. Categoria: {text}"
            page.open(ft.SnackBar(ft.Text(informativo, color="WHITE"),bgcolor="black"))
                
            
        except ValueError:
            # Exibe Snackbar com mensagem de erro
            page.open(ft.SnackBar(ft.Text("Por favor, insira valores numéricos válidos para peso e altura.", color="WHITE"),bgcolor="black"))
            imput_peso.value = ""
            imput_altura.value = ""
        page.update()

    # Campos e botões
    texto1 = ft.Text("Calculadora de Índice de Massa Corporal", size=25, color="white")
    imput_peso = ft.TextField(label="Escreva o peso(kg)...")
    imput_altura = ft.TextField(label="Escreva a altura(m)...")
    calcular_imc = ft.ElevatedButton("CALCULAR IMC", bgcolor="BLACK", color="WHITE", width=200, on_click=calculo_imc)

    # Layout
    page.add(
        ft.Row("", alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row([texto1], alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row("", alignment="center"),
        ft.Row([imput_peso], alignment="center"),
        ft.Row([imput_altura], alignment="center"),
        ft.Row([calcular_imc], alignment="center")
    )

ft.app(target=main)
