def mostra_linha():
    """
    Mostra uma linha de separação.
    """
    print('-' * 50)


# Exemplo de uso da função mostra_linha
mostra_linha()

print("Aluguel de Carros  com a maior frota de Brasil | Localiza")

mostra_linha()

print("Seja bem Vindo!")

mostra_linha()

nome = input("Digite seu nome:")
print(f"Olá {nome} estamos felizes em tê-lo conosco.")

mostra_linha()

print("Selecione o carro que deseja alugar:")
print("1 - BMW")
print("2 - MUSTANG")
print("3 - HB20")
print("4 - FUSCA")
print("5 -CIVIC")
print("0 - SAIR")

mostra_linha()

codigo = int(input("Digite o codigo do produto:"))

import os
os.system('cls')

#Use match-case para mostrar o preço com base mo código
match codigo:
    case 1:
        print("Alugue uma BMW - por R$ 400,00")
    case 2:
        print("Alugue um MUSTANG - por R$ 450,00")
    case 3:
        print("Alugue um HB20 - por R$ 500,00")
    case 4:
        print("Alugue um FUSCA - por R$ 550,00")
    case 5:
        print("Alugue um CIVIC - por R$ 408,98")
    case 0:
        print("Saindo do Programa...")
        exit()
    case _:
        print("Codigo inválido. Por favor, tente novamente.") 