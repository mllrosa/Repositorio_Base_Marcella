## A empresa já possui um banco de dados chamado empresa.db, que contém a tabela funcionarios com os campos:
## id, nome, cargo, salario, departamento
def linha():
    print('-'*30)

import sqlite3 as sq
banco = sq.connect("empresa.db")
cursor = banco.cursor()

# Liste apenas os nomes e salários de todos os funcionários.
cursor.execute("SELECT nome, salario FROM funcionarios")
print(cursor.fetchall())
linha()

# Mostre todos os dados do funcionário cujo nome é "Carla".
cursor.execute("SELECT * FROM funcionarios WHERE nome = 'Carla'")
print(cursor.fetchall())
linha()

# Exiba o nome e o cargo de todos os funcionários do departamento "TI".
cursor.execute("SELECT nome, cargo FROM funcionarios WHERE departamento = 'TI'")
print(cursor.fetchall())
linha()