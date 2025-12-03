#imprimir numeros impares até o numero digitado pelo usuario

x = 1
contador = 0

quantidade_impares = int(input('Digite a quantidade de ímpares que deseja gerar: '))

while contador < quantidade_impares:
    print(x)
    x += 2
    contador += 1