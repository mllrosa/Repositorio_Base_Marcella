import csv

with open('seuarquivo.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for i, linha in enumerate(leitor):
        linha_junta = ' '.join(linha)
        if 'Damian Ramirez' in linha_junta:
            print(f'Nome encontrado na linha {i + 1}')