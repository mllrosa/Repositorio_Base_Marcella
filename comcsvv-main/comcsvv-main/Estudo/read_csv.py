import csv 

with open('dados.csv', encoding='utf-8') as arquivo_csv:
    for linha in arquivo_csv:
        print(linha)

        

""" 
with open("dados.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for linha in arquivo_csv:
        print(linha)
"""
