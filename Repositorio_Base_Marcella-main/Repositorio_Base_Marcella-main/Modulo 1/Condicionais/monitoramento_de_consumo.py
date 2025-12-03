#1. O programa deve solicitar ao usuário: distância percorrida (em km) e quantidade de combustível gasto (em litros)

nome_do_usuario = input('Ola! Seja bem-vindo a nossa central de atendiment, aqui o ajudaremos a calcular e monitorar o seu consumo de combustivel. Por favor insira seu nome:')
distancia_percorrida = float (input('digite a distancia oercorrida em quilometros:'))
combustivel_gasto = float (input('digite a quantidade de combustivel gasto(em litros):'))

#2. O programa deve calcular o consumo médio: consumo_medio = distancia / litros
consumo_medio = distancia_percorrida / combustivel_gasto

print(f'o consumo medio  do seu veiculo foi de {consumo_medio} quilometro por litro')

#3. O valor calculado deve ser exibido junto com uma mensagem de desempenho
if consumo_medio < 8.0:
    print(f'Sr(a){nome_do_usuario}, voce obteve um alto consumo')

elif 8.0 < consumo_medio < 12.0:
    print(f'Sr(a) {nome_do_usuario}, voce obteve um consumo moderado')

else:
    print(f'Sr(a){nome_do_usuario}, Parabens, seu consumo foi moderado')
