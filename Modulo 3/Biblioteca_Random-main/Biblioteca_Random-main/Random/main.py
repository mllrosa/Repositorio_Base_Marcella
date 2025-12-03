# Tente aplicar o Random nesses exercícios
import random
#   👑 Cara ou Coroa
# while True:
#     lista = ['Cara', 'Coroa']
#     # escolha = input("escolha 1 para Cara ou 2 para Coroa:")
#     # lista.remove('Cara' if escolha == 1 else 'Coroa')
#     escolha = input("escolha Cara ou Coroa:")
#     lista.remove(escolha)
#     moeda = random.choice(lista)
#     print(f"Você errou! O resultado foi {moeda} 🥱!")
#     break



# #   🧑🏻‍🎓 Sorteio de aluno
# aluno = random('Milly', 'MaLL', 'MeLL')
# print(f"O aluno sorteado foi {aluno}")

# #   🎲 Dado de 6 lados
# dado = random.randint(1,6)
# print(F"O numero do dado é {dado}") 

#   🔢 Adivinhe o número

num = random.randint(1,60)
while True:
    try:
        escolha = int(input("Escolha um numero de 1 à 60:"))
    except:
            print('O numero deve ser um numero de 1 à 60:') 

    if escolha == num:
        numnovo = random.randint(1,60)
        print(f"Você errou o numero sorteado!")
    else:
        print(f"Você errou o numero sorteado!")