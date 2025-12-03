import csv

with open("dados.csv",newline="",encoding="utf-8") as arquivo:
    arquivo_csv = csv.DictReader(arquivo)

    #dados = list(arquivo_csv)
    
    for linha in arquivo_csv:
        autores = linha["Author(s)"]
        
        if linha ["Author(s)"] == "Fortunato, Victoria Della Ventura, Hernández, Nahuel Nicolás, Vázquez, Damián Ramírez":
            linha["Author(s)"].split(',')
            print(linha["Author(s)"])