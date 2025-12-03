primeiro_nome_vendedor = (input('Nome do vendedor:'))
salario_fixo = float(input('Inserir seu salario fixo:'))
montante_de_vendas = float(input('Inserir o montante total das vendas efetuadas:'))

valor_a_receber_comissao = (salario_fixo * 0.15)
valor_a_receber_total = valor_a_receber_comissao + salario_fixo

print(f'O total de comissão a receber é: {valor_a_receber_comissao}')
print(f'O total a receber é: {valor_a_receber_total}')

