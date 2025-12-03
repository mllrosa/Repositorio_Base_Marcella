print("Códigos de produtos: ")
print("1 - Pizza Portuguesa ")
print("2 - Pizza de Doce de Leite ")
print("3 - Pizza de Calabresa ")
print("4 - Pizza de Morango com Chocolate")
print("5 - Pizza de Mussarela ")
print("0 - SAIR")
print("")

# Solicita o código do produto ao usuário
codigo = int(input("Digite o código do produto: "))

# Usa match-case para mostrar o preço com base no código
match codigo:
    case 1:
        print("Produto: Pizza Portuguesa - Preço: R$ 45,00")
    case 2:
        print("Produto: Pizza de Doce de Leite - Preço: R$ 30,00")
    case 3:
        print("Produto: Pizza de Calabresa - Preço: R$ 50,00")
    case 4:
        print("Produto: Pizza de Morango com Chocolate - Preço: R$ 60,00")
    case 5:
        print("Produto: Pizza de Mussarela - Preço: R$ 29,00")

    case 0:
        print("Saindo do programa...")
        exit() #encerra o programa se o codigo se for 0

    case _:
        print("Código inválido. Por favor, tente novamente.")