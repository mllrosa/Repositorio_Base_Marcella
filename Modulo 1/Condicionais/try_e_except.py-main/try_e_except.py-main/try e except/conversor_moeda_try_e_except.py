print("COVERSOR DE MOEDA")
# Definiçao de constante para a taxa de câmbio


DOLAR = 5.50


try:
    valor_em_dolar = float(input("Digite o valor em dólares: "))
    valor_em_real = valor_em_dolar * DOLAR
except:
    print("Houve um erro, tente novamente e digite os numeros corretamente.")


print(f"O valor convertido em reais é: {valor_em_real:.2f}")