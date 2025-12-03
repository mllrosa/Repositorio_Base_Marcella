nome_produto = input('Digite o nome do produto:')
preço = float(input('Digite o preço do produto:'))
desconto = float(input('Digite o percentual de desconto:'))

valor_de_desconto = preço * desconto / 100
preço_final = preço - valor_de_desconto

print(f'Produto: {nome_produto} - Preço final: R$ {preço_final}')


