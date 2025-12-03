import csv

with open("dados.csv",newline="",encoding="utf-8") as arquivo:
    arquivo_csv = csv.DictReader(arquivo)

    nome = "Damián Ramírez"

    for linha in arquivo_csv:
        autores = linha["Author(s)"].split(',')
        autores = [a.strip() for a in autores]
        
        if nome in autores:
            print(nome)

"""
split(',') separa as str pela virgula
strip() limpa os espacos antes e depois de cada str

newline="" evita que o python insira linhas em branco ao ler ou gravar
encoding="utf-8" define como os caracteres serao lidos
csv.DictReader lê cada linha como um dicionario com as colunas sendo chaves

read + 'r' horrivel, so pra ler tudo como texto
"""