
import csv

with open('dados.csv', encoding='utf-8') as arquivo_csv:
    #for _ in range(2):
    #arquivo_csv.readline()
    #linha = arquivo_csv.readline().strip()
    
    contador = 1
    for linha in arquivo_csv:
        if contador == 3 or contador == 5 or contador == 7:
            linha = linha.strip()
            elementos = linha.split(',')
            quantidade_elementos = len(elementos)

            print(f'Elementos da linha {contador}: \n {elementos} \n ou seja {quantidade_elementos} elementos')
            print(f'A linha {contador} tem {quantidade_elementos} elementos.')

        contador += 1