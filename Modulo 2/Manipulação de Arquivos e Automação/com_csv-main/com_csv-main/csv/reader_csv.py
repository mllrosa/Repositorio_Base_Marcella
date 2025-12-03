import csv # CSV (Comma-Separated Values) Valores Separados por Vírgula 
# Lendo e exibindo os dados de um arquivo
with open("dados.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",") # Define a vírgula , como delimitador (ou seja, separador de colunas)
    for linha in arquivo_csv: # Para cada linha um print?
        print(linha)




exemplefile = open("dados.csv")
exemplereader = csv.reader(exemplefile)
exampledata = list(exemplereader) # Coverte o conteudo para uma lista
"""Checando quantos elementos há na linha 1
for i in range(len(exampledata[1])):
    print(exampledata[1][i])"""
print(exampledata[1] [0])
print(exampledata[1] [1])
print(exampledata[1] [2])
print(exampledata[1] [3])
print(exampledata[1] [4])
# Imprimir tudo: print = exampledata 
exemplefile.close()




examplefile = open('dados.csv')
examplereader = csv.reader(examplefile)
for row in examplereader:
    print('Row #' + str(examplereader.line_num) + '' + str(row))
# Imprime cada linha com seu número correspondente




with open('dados.csv', 'w') as arquivo:
    arquivo_csv = csv.writer(arquivo)
    # Apaga tudo oqie estava escrito e escreve...
    arquivo_csv.writerow(["cor \t idade"])
    arquivo_csv.writerow(["corr \t idadee"])

    
    
    
    
    with open('dados.csv', 'w', newline='') as arquivo:
    arquivo_csv = csv.writer(arquivo)
    arquivo_csv.writerow(["cor", "idade"])
    arquivo_csv.writerow(["azul", "25"])
    # Formatacao mais correta e que cria colunas e linhas
    # E tambem nao apaga tudo, adiciona

