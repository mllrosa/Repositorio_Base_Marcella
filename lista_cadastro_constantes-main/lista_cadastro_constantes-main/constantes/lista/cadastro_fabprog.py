import os

nomes_cadastrados = ["Melissa", "Gab", "Julia"]

print("Olá, seja bem vindo a central de cadastro da FABPROG!")
while True:

    print("Há algo que gostaria de fazer?")
    print("1 - REALIZAR UM CADASTRO")
    print("2 - REMOVER ALUNO DA TURMA")
    print("3 - VER NOMES CADASTRADOS")
    print("4 - SAIR DO PROGRAMA")

    codigo = int(input())

    match codigo:
        case 1:
            os.system('cls')
            nome_usuario = input("Para iniciarmos seu cadastro digite seu nome: ")
            nomes_cadastrados.append(nome_usuario)
            print("Muito bem, você foi cadastrado no nosso programa.")
            print("Até o momento, as pessoas cadastradas na sua turma são:", nomes_cadastrados)

        case 2:
            os.system('cls')
            nome_remover = input("Digite o nome do aluno que deseja remover da turma: ")
            nomes_cadastrados.remove(nome_remover)
            print("Muito bem, o aluno foi removido:")
            print("Até o momento, as pessoas cadastradas na sua turma são:", nomes_cadastrados)
            print("-----------------------------------------------------------------------------")
        case 3:
            os.system('cls')
            print("Até o momento, as pessoas cadastradas na sua turma são:", nomes_cadastrados)

        case 4:
            os.system('cls')
            print("Fechando o programa...")

        case _:
            print("Código inválido. Por favor, tente novamente.")