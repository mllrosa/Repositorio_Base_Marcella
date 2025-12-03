import csv 

with open("dados.csv" , newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha["nome"]
        nota = float(linha["nota"])
        if nota > 7:
            print(f"{nome} passou com {nota}")

            media = sum(float(linha["nota"]) for linha in leitor) / len(linha["nota"]) 
            len(linha["nota"])
            print("sua media é:", media)









"""#Leia o conteúdo do arquivo CSV.
with open("dados.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",") # Define a vírgula , como delimitador
    for linha in arquivo_csv: # Para cada linha um print
        print(linha)

    #Mostre o nome de todos os alunos com nota maior ou igual a 7.

"""