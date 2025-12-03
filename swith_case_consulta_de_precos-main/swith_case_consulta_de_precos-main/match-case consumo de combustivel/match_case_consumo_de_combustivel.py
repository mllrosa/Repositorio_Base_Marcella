#switch case
# Solicita os dados do usuário

distancia_percorrida = float(input("Digite a distância percorrida em km: "))
combustivel_gasto = float(input("Digite a quantidade de combustível gasto em litros: "))

# Calcula o consumo médio
consumo_médio = distancia_percorrida / combustivel_gasto

#Classifica o consumo usando match-case
match consumo_médio: #match consumo_medio: abre o bloco de "casos".
    case valor if valor < 8:
        print("Consumo menor que 8 km/1 - DESEMPENHO RUIM")
    case valor if valor < 12:
        print("Consumo entre 8 e 12 km/1 - DESEMPENHO MÉDIO")
    case _:
        print("Consumo maior ou igual a 12 km/1 - ÓTIMO DESEMPENHO")
        