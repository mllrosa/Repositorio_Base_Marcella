#1. Solicita o nome do sistema de IA
nome_ia = (input('Informe o nome do sistema de IA:'))

#2. Recebe sua pontuação de performance (de 0 a 100)
pontuacao = float(input('Informe a pontuaçao obtida pelo sistema:'))

#3. Exibe a classificação do nível de inteligência com base nessa pontuação

if 0 <= pontuacao <= 39.9:
    print(f'Segundo os dados fornecidos {nome_ia}, é uma IA em Treinamento 🍼')

elif 40.0 <= pontuacao <= 69.9:
    print(f'Segundo os dados fornecidos {nome_ia}, obteve uma pontuação Intermediária 🧠 ')

elif 70.0 <= pontuacao <= 89.9:
    print(f'Informamos que {nome_ia}, é uma IA Otimizada 🚀')
    
elif 90.0 <= pontuacao <= 100:
    print(f'Informamos que {nome_ia}, teve uma pontução de IA Avançada (nível Skynet 🤯 )')

elif pontuacao > 100:
    print(f'Informamos que houve um erro com {nome_ia}, IA fora da escala! ⚠️ ')

else:
    print(f'Informamos que houve um erro com {nome_ia}, a pontuação é inválida! ❌')
