# 🐼 Exercícios de Pandas + Random
import pandas as pd
import random

# # 💡 1) Gerador de Notas Aleatórias
# # Crie um programa que gere as notas de 10 alunos para 3 matérias: Matemática, Português e Ciências.
# # As notas devem ser números aleatórios de 0 a 10 (inteiros).

# # 1. Crie um DataFrame com as colunas ["Aluno", "Matemática", "Português", "Ciências"]
# alunos = ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ"]

# notas = {
#     'Aluno': alunos,
#     'Matemática': [random.randint(0, 10) for i in (alunos)],
#     'Português': [random.randint(0, 10) for i in (alunos)],
#     'Ciências': [random.randint(0, 10) for i in (alunos)],
# }
# df_notas = pd.DataFrame(notas)
# print("Notas dos Alunos:")
# print(df_notas)


# # 2. Calcule a média geral de cada aluno em tres casas decimais e adicione uma nova coluna "Média" ao DataFrame.
# print("\nNotas com Média:")
# df_notas['Média'] = df_notas[['Matemática', 'Português', 'Ciências']].mean(axis=1).round(1)
# print(df_notas)


# # 3. Mostre o aluno com a maior média.
# melhor_aluno = df_notas.loc[df_notas['Média'].idxmax()]
# print("\nAluno com a maior média:")
# print(melhor_aluno)



# # 📊 2) Vendas Aleatórias de Lojas
# # Crie um DataFrame que simule as vendas de 5 lojas diferentes, com valores diários gerados aleatoriamente entre 100 e 1000 reais durante 7 dias.
# # Desafios:

# # Calcule o total de vendas por loja.
# lojas = ["Loja A", "Loja B", "Loja C", "Loja D", "Loja E"]
# dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
# vendas = {
#     'Loja': lojas,
#     'Segunda': [random.randint(100, 1000) for _ in lojas],
#     'Terça': [random.randint(100, 1000) for _ in lojas],
#     'Quarta': [random.randint(100, 1000) for _ in lojas],
#     'Quinta': [random.randint(100, 1000) for _ in lojas],
#     'Sexta': [random.randint(100, 1000) for _ in lojas],
#     'Sábado': [random.randint(100, 1000) for _ in lojas],
#     'Domingo': [random.randint(100, 1000) for _ in lojas],
# }
# df_vendas = pd.DataFrame(vendas)
# print("Vendas das Lojas:")
# print(df_vendas)
# df_vendas['Total de Vendas'] = df_vendas[dias].sum(axis=1)
# print("\nTotal de Vendas por Loja:")
# print(df_vendas[['Loja', 'Total de Vendas']])


# # Mostre qual loja vendeu mais na semana.
# loja_mais_vendeu = df_vendas.loc[df_vendas['Total de Vendas'].idxmax()]
# print("\nLoja que mais vendeu na semana:")
# print(loja_mais_vendeu)

# # Calcule o valor médio diário geral (média de todas as lojas e dias).
# valor_medio_diario = df_vendas[dias].mean().mean()
# print(f"\nValor médio diário geral: R$ {valor_medio_diario:.2f}")



# 📦 3) Controle de Estoque Aleatório
# Simule um estoque de 8 produtos.
# Cada produto deve ter:

# Nome (Produto 1, Produto 2, etc.)
# Quantidade (aleatória entre 10 e 100)
# Preço (aleatório entre 5.0 e 100.0)
# Desafios:

# Adicione uma coluna chamada "Valor Total" (quantidade * preço).
# Descubra qual produto tem o maior valor total.
# Mostre apenas os produtos com valor total acima da média.



# # 🧠 4) Sorteio de Dados Aleatórios
# # Crie um programa que simule 50 lançamentos de dado (1 a 6) e salve os resultados em um DataFrame.
# # Desafios:
# dados = {
#     'Lançamento': [random.randint(1, 6) for _ in range(50)]
# }

# # Mostre quantas vezes cada número foi sorteado.
# df_dados = pd.DataFrame(dados)
# print("Lançamentos de Dados:")
# print(df_dados)
# contagem_numeros = df_dados['Lançamento'].value_counts().sort_index()
# print("\nContagem de cada número sorteado:")
# print(contagem_numeros)


# # Crie uma coluna adicional chamada "Par/Ímpar".
# df_dados['Par/Ímpar'] = df_dados['Lançamento'].apply(lambda x: 'Par' if x % 2 == 0 else 'Ímpar')
# print("\nLançamentos com Par/Ímpar:")
# print(df_dados)

# # Mostre quantas vezes saíram números pares e ímpares.
# contagem_par_impar = df_dados['Par/Ímpar'].value_counts()
# print("\nContagem de Números Pares e Ímpares:")
# print(contagem_par_impar)
