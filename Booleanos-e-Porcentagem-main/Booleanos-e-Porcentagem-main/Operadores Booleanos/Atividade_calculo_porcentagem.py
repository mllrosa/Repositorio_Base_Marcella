#Cálculo de Porcentagem de um Número.
#• O programa deve calcular e exibir o valor que corresponde a essa
# porcentagem do total. Exemplo: se o usuário digitar 200 como
#valor total e 15 como porcentagem, o programa deverá calcular
#que 15% de 200 é 30.
#• Exemplo de fórmula:
#valor_parte = valor_total * (porcentagem / 100)

#1. receber a variavel valor_total [float]
#2. receber a porcentagem
#3. calcular a fórmula
#4. imprimir o resultado da fórmula

valor_total = float(input('Insira o valor total:'))

valor_porcentagem = float(input('Insira a porcentagem:'))

resultado = valor_total * (valor_porcentagem / 100 )
print(resultado)

#Cálculo de Desconto em um Produto.
#Se o usuário informar que o preço original é 100 e o desconto é de 20%, o programa deverá calcular que o valor do desconto é 20 e, consequentemente, o preço final será 80.
# Exemplo de fórmula: valor_desconto = preco_original * (porcentagem_desconto / 100) preco_final = preco_original - valor_desconto

preço_original = float(input('Insira o preço:'))
porcentagem_desconto = float(input('Insira a porcentagem de desconto:'))
valor_desconto = preço_original * (porcentagem_desconto / 100 )
preço_final = preço_original - valor_desconto
print(f'valor a pagar é {preço_final}')
print(f'o desconto foi de {valor_desconto}')