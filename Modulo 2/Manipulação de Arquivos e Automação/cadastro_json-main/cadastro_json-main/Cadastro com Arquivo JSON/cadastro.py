import json, os

Nome_arquivo = "dados.json"

def literminal():
    os.system('cls')

def carregar():
    with open(Nome_arquivo, 'r') as arquivo:
        literminal()
        return json.load(arquivo)


def salvar(dados):
    with open(Nome_arquivo, "w") as arquivo:
        literminal()
        json.dump(dados, arquivo)


def criar():
    nome = input("Nome:")
    idade = input("Idade:")
    email = input("Email:")

    dados = carregar()
    dados.append({"nome": nome, "idade": idade, "email": email})
    literminal()
    salvar(dados)
    print("Salvo!")


def listar():
    dados = carregar()
    literminal()
    for p in dados:
        print(p)


def atualizar():
    nome = input("Nome para atualizar: ")
    dados = carregar()
    for linha in dados:
        if linha["nome"] == nome:
            linha["idade"] = input("Nova idade: ")
            linha["email"] = input("Novo email: ")
            linha["telefone"] = input("Novo telefone: ")
            salvar(dados)
            literminal()
            print("Atualizado!")
            return
    print("Nome não encontrado.")


def deletar():
    nome = input("Nome para deletar: ")
    dados = carregar()
    for linha in dados:
        if linha["nome"] == nome:
            dados.remove(linha)
            salvar(dados)
            print("\n\n ❌ Deletado! \n\n")
            return
    print("Nome não encontrado.")


def menu():
    opcao = 0
    while opcao !=5:
        print("\n1 - Criar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("5 - Sair")
        opcao = int(input("Escolha: "))
        if opcao == 1:
            criar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        elif opcao == 5:
            literminal()
            break

print("Seja bem vinda(o)! O que gostaria de fazer?")
menu()
with open(Nome_arquivo, "+a") as arquivo:
    arquivo.seek(0)
    try:
        json.load(arquivo)
    except:
        arquivo.write("[]")