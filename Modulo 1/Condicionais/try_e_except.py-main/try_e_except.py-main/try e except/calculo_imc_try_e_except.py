print("CALCULADORA DE IMC")


try:
    peso = float(input('Insira o peso:'))
    #print(peso)


    altura = float(input('Insira a altura:'))
    #print(altura)
except:
    print("Houve um erro, tente novamente e digite os numeros corretamente.")


imc = peso / (altura **2)
print("Seu IMC é", imc)
