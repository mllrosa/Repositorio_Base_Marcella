import matplotlib.pyplot as plt
import numpy as np

# Dados
modulos = ["Módulo 1", "Módulo 2", "Módulo 3"]
faltas = [80, 8, 2]  # número de faltas
presenca = [20, 92, 98]  # número de presenças

# Configurando posições das barras
x = np.arange(len(modulos))  # posições dos módulos
largura = 0.35  # largura de cada barra

# Criando o gráfico
fig, ax = plt.subplots()

barras1 = ax.bar(x - largura/2, faltas, width=largura, color='red', label="Faltas")
barras2 = ax.bar(x + largura/2, presenca, width=largura, color='green', label="Presença")

# Adicionando valores em cima das barras
for barra in barras1:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura + 1, f"{altura}", ha='center', va='bottom', fontsize=9)
for barra in barras2:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura + 1, f"{altura}", ha='center', va='bottom', fontsize=9)

# Ajustes do gráfico
ax.set_xticks(x)
ax.set_xticklabels(modulos)
ax.set_ylim(0, 110)  # Aumentei o limite para 110 para caber os valores altos
ax.set_title("Frequência por Módulo")
ax.legend()

plt.tight_layout()
plt.show()