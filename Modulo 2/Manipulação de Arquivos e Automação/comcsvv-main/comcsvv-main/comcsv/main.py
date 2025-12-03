import csv

with open("dados.csv",newline="",encoding="utf-8") as arquivo:
    arquivo_csv = csv.DictReader(arquivo)

    nome_procurado = "Damián Ramírez"

    for linha in arquivo_csv:
        if linha ["Author(s)"] == "Fortunato, Victoria Della Ventura, Hernández, Nahuel Nicolás, Vázquez, Damián Ramírez":
            linha["Author(s)"].split(',')
            print(linha["Author(s)"])






    for linha in arquivo_csv:
        autores = linha["Author(s)"].split(',')
        autores = [a.strip() for a in autores]

        if nome_procurado in autores:
            print(nome_procurado)