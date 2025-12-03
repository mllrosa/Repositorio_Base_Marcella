# 💵 CONVERSOR DÓLAR ↔ REAL (SIMPLES)
import flet as ft
import requests

def main(page: ft.Page):
    # Configuração básica da página
    page.title = "Conversor de Moedas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.window.width = 380
    page.window.height = 670
    
    # Variáveis
    cotacao_atual = 5.0  # Valor padrão
    
    # Elementos da interface
    titulo = ft.Text(
        "💵 Conversor Dólar ↔ Real",
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Informações da cotação
    texto_cotacao = ft.Text(
        f"Cotação: R$ {cotacao_atual}",
        size=14,
        text_align=ft.TextAlign.CENTER
    )
    
    # Campo para Dólar
    campo_dolar = ft.TextField(
        label="Valor em Dólar",
        prefix_text="$ ",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300
    )
    
    resultado_real = ft.Text(
        "R$ 0,00",
        size=18,
        weight=ft.FontWeight.BOLD
    )
    
    # Campo para Real
    campo_real = ft.TextField(
        label="Valor em Real", 
        prefix_text="R$ ",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300
    )
    
    resultado_dolar = ft.Text(
        "$ 0.00",
        size=18,
        weight=ft.FontWeight.BOLD
    )
    
    # Botões
    def converter_dolar_click(e):
        try:
            if campo_dolar.value:
                valor = float(campo_dolar.value)
                resultado = valor * cotacao_atual
                resultado_real.value = f"R$ {resultado:,.2f}"
                page.update()
        except:
            resultado_real.value = "Erro!"
            page.update()
    
    def converter_real_click(e):
        try:
            if campo_real.value:
                valor = float(campo_real.value)
                resultado = valor / cotacao_atual
                resultado_dolar.value = f"$ {resultado:,.2f}"
                page.update()
        except:
            resultado_dolar.value = "Erro!"
            page.update()
    
    def atualizar_cotacao_click(e):
        try:
            # Tenta buscar cotação atual
            url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
            resposta = requests.get(url, timeout=5)
            dados = resposta.json()
            nova_cotacao = float(dados['USDBRL']['bid'])
            texto_cotacao.value = f"Cotação: R$ {nova_cotacao:.2f}"
            nonlocal cotacao_atual
            cotacao_atual = nova_cotacao
            page.update()
        except:
            texto_cotacao.value = "Erro ao buscar cotação"
            page.update()
    
    def limpar_click(e):
        campo_dolar.value = ""
        campo_real.value = ""
        resultado_real.value = "R$ 0,00"
        resultado_dolar.value = "$ 0.00"
        page.update()
    
    # Layout
    page.add(
        titulo,
        ft.Divider(height=20),
        
        texto_cotacao,
        ft.ElevatedButton(
            "Atualizar Cotação",
            on_click=atualizar_cotacao_click,
            width=300
        ),
        
        ft.Divider(height=30),
        
        campo_dolar,
        ft.ElevatedButton(
            "Converter para Real",
            on_click=converter_dolar_click,
            width=300
        ),
        resultado_real,
        
        ft.Divider(height=20),
        
        campo_real,
        ft.ElevatedButton(
            "Converter para Dólar", 
            on_click=converter_real_click,
            width=300
        ),
        resultado_dolar,
        
        ft.Divider(height=20),
        
        ft.ElevatedButton(
            "Limpar",
            on_click=limpar_click,
            width=300
        )
    )
    
    # Busca cotação inicial
    atualizar_cotacao_click(None)

ft.app(target=main)