# TABUADA
try:
    numero = int(input("Digite um numero para ver a tabuada: "))
except:
    print("Houve um erro, tente novamente e digite os numeros corretamente.")


for i in range(1, 11):
    print(f"{i}x{numero} = {i * numero}")