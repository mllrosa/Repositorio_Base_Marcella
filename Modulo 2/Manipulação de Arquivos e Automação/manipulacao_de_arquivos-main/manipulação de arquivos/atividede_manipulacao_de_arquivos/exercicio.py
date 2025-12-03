arquivo = open('cadastro.txt', 'w', encoding = 'utf-8')
arquivo.write('CADASTROS:\n')
arquivo.close()

while True:
    print('Segue o formulario para um novo cadastro.')
    nome_usuario = input("Digite um nome para cadstro:")
    email_usuario = input("Digite o e-mail:")

    arquivo = open('cadastro.txt', 'a', encoding = 'utf-8')
    arquivo.write(f'PESSOA:{nome_usuario}')
    arquivo.write(f'     E-MAIL CORESPONDENTE: {email_usuario}\n')
    arquivo.close()

    arquivo = open('cadastro.txt', 'r', encoding = 'utf-8')
    conteudo = arquivo.read()
    print("Até o momento, os usuarios cadastrados são:")
    print(conteudo)
    arquivo.close()
    simounao = int(input("gostaria de realizar mais um cadastro?\n 1 - SIM / 2 - NÃO:"))

    if simounao == 2:
        break

print('Fechando...')

"""
nome = input("Digite o nome: ")
email = input("Digite o e-mail")

arquivo = open("pessoa.txt", "a")
arquivo.write(nome + "|" + email + "\n")
arquivo.close()
"""

"""
MODE
r - leitura
a - append
w - escrita
x - criar arquivo
r+ - leitira + escrita
"""
# arquivo.readable()
# retorna se o arquivo pode ser lido ou nao

# arquivo.readline()
# le uma linha

# arquivo.readlines()
# le o arquivo e tranforma o conteudo em listas?

