senha = input("Digite a senha: ")

while senha != "123456":
    senha = input("Digite a senha: ")
    if senha == "123456":
        print("Senha correta!")
    else:
        print("Senha incorreta! Tente novamente")


