numero1 = input("Digite o primeiro numero: ")
numero2 = input("Digite o segundo numero: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)

    print(f"A soma dos numeros é: {numero1 + numero2}")

except:
    print("Digite um número correto!")