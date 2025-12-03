# Criar um arquivo csv e adicionar linhas

import csv

dados = [
    ['a', 'b', 'c'],
    ['1', 2, '3']
]


with open('sequencias.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

nova_linha = ['x', 'y', 'z']
with open('sequencias.csv', mode='a', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(nova_linha)