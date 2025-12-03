nome_do_usuario = input('Olá! Gostaria de monitorar sua saúde com base no cálculo de IMC? \nSe sim, começe nos dizendo seu nome, por favor:')

peso = float(input('Agora, nos informe seu peso:'))
#print(peso)

altura = float(input('Informe também sua altura:'))
#print(altura)

imc = peso / (altura **2)

#exibir:
#O valor calculado
print(f'Segundo os dados fornecidos, informamos que {nome_do_usuario}, tem um IMC de {imc}')

#exibir:
#Uma mensagem de orientação baseada no resultado

if  imc < 18.5:
    print(f'E que e que o(a) mesmo(a), está abaixo do peso')

elif 18.5 <= imc <= 24.9:
    print(f'E que e que o(a) mesmo(a), está com um peso normal')

elif 25.0 <= imc <= 29.9:
    print(f'E que e que o(a) mesmo(a), está com sobrepeso')
    
elif 30.0 <= imc <= 34.9:
    print(f'E que e que o(a) mesmo(a), está com besidade Grau I)')

elif 35.5 <= imc <= 39.9 :
    print(f'E que e que o(a) mesmo(a), está com besidade Grau II')

else:
    print(f'E que e que o(a) mesmo(a), está com besidade Grau III (mórbida)')

    
