# Um banco loja.db já possui a tabela vendas com os campos: id, produto, quantidade, preco_unitario, cliente
def linha():
    print('-'*30)

import sqlite3 as sq
banco = sq.connect("loja.db")
cursor = banco.cursor()

# Mostre apenas o produto e o cliente de todas as vendas.
cursor.execute("SELECT cliente,produto FROM vendas")
print(cursor.fetchall())
linha()

# Liste todas as vendas feitas pelo cliente "João".
cursor.execute("SELECT quantidade FROM vendas WHERE cliente = 'João' ")
print(cursor.fetchall())
linha()

# Exiba os produtos cujo preço unitário seja maior que 50.
cursor.execute("SELECT produto FROM vendas WHERE preco_unitario >50 ")
print(cursor.fetchall())
linha()
