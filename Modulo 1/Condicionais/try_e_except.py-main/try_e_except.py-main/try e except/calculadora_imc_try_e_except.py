print("CALCULADORA")
   
# FUNCOES
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: divisao por zero"
    return a / b


# MENU?
print("Escolha uma das operações disponíveis:")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")


# wwwww 1
try:
    operacao = int(input("Digite o número da operação: "))
except ValueError:
    print("Houve um erro: digite o número conforme no menu de escolha.")
    exit()

    

# RECEBER NUMEROS
# wwwww 2
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Houve um erro: digite os números corretamente.")




match operacao:
    case 1 :
        resultado = somar(numero1, numero2)
        print("O resultado é:", resultado)
    case 2 :
        resultado = subtrair(numero1, numero2)
        print("O resultado é:", resultado)
    case 3 :
        resultado = multiplicar(numero1, numero2)
        print("O resultado é:", resultado)
    case 4 :
        resultado = dividir(numero1, numero2)
        print("O resultado é:", resultado)
    case _:
        print("Houve um erro, tente novamente!")