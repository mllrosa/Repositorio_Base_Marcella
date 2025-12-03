#o break interrompe o loop

soma = 0

while True:
    x = int(input('Digite um número para ser somado: \n ou \n 0 para sair:'))
    if x == 0:
        break
    soma += x
print(f'A soma dos números digitados é {soma}')