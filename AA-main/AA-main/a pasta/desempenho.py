import matplotlib
matplotlib.use("Agg")  # evita abrir janela GUI
import matplotlib.pyplot as plt
import flet as ft
from io import BytesIO

def main(page: ft.Page):
    # Dados
    modulos = ["Módulo 1", "Módulo 2", "Módulo 3"]
    nota = [80, 70, 85]
    frequencia = [90, 75, 100]

    largura = 0.35
    x = range(len(modulos))
    
    # Criando o gráfico
    plt.figure(figsize=(6,4))
    plt.bar([i - largura/2 for i in x], nota, width=largura, color='skyblue', label="Nota")
    plt.bar([i + largura/2 for i in x], frequencia, width=largura, color='salmon', label="Frequência (%)")
    
    for i, n in enumerate(nota):
        plt.text(i - largura/2, n + 2, str(n), ha='center')
    for i, f in enumerate(frequencia):
        plt.text(i + largura/2, f + 2, f"{f}%", ha='center')
    
    plt.xticks(x, modulos)
    plt.ylim(0, 105)
    plt.title("Nota e Frequência do Aluno por Módulo")
    plt.legend(loc='upper left')
    
    # Salva em memória
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()  # fecha a figura para liberar memória
    
    # Mostra no Flet
    img = ft.Image(src=buf.getvalue())
    page.add(img)

ft.app(target=main)
