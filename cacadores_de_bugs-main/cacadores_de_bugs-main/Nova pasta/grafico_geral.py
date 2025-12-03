import matplotlib.pyplot as plt

# Dados
modulos = ["Módulo 1", "Módulo 2", "Módulo 3"]
nota = [80, 70, 85]        # notas do aluno
frequencia = [90, 75, 100]  # frequência em %

# Largura das barras
largura = 0.35
x = range(len(modulos))

# Criando as barras
plt.bar([i - largura/2 for i in x], nota, width=largura, color='skyblue', label="Nota")
plt.bar([i + largura/2 for i in x], frequencia, width=largura, color='salmon', label="Frequência (%)")

# Valores em cima das barras
for i, n in enumerate(nota):
    plt.text(i - largura/2, n + 2, str(n), ha='center')
for i, f in enumerate(frequencia):
    plt.text(i + largura/2, f + 2, f"{f}%", ha='center')

# Ajustes do gráfico
plt.xticks(x, modulos)
plt.ylim(0, 105)  # adiciona espaço extra para barras altas
plt.title("Nota e Frequência do Aluno por Módulo")
plt.legend(loc='upper left')  # legenda no topo à esquerda
plt.show()
