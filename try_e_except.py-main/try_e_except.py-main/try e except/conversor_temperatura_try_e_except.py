print("COVERSOR DE TEMPERATURA - De Celsius para Kelvin")
try:
    celsius = float(input("Digite a temperatura em celcius:"))
except:
    print("Houve um erro, tente novamente e digite os numeros corretamente.")


em_kelvin = celsius + 273.15


print(f"A temperatura em kelvin é: {em_kelvin}k")