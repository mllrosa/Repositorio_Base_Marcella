import matplotlib.pyplot as plt
import numpy as np

# Dados
modulos = ["Módulo 1", "Módulo 2", "Módulo 3"]
prova1 = [40, 70, 85]
prova2 = [60, 65, 90]

# Configurando posições das barras
x = np.arange(len(modulos))  # posições dos módulos
largura = 0.35  # largura de cada barra

# Criando o gráfico
fig, ax = plt.subplots()

barras1 = ax.bar(x - largura/2, prova1, width=largura, color='skyblue', label="Prova 1")
barras2 = ax.bar(x + largura/2, prova2, width=largura, color='salmon', label="Prova 2")

# Adicionando valores em cima das barras
for barra in barras1:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura + 2, f"{altura}", ha='center')
for barra in barras2:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura + 2, f"{altura}", ha='center')

# Ajustes do gráfico
ax.set_xticks(x)
ax.set_xticklabels(modulos)
ax.set_ylim(0, 100)
ax.set_title("Notas por Módulo")
ax.legend()

plt.show()
