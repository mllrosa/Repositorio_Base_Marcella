import sqlite3 as sq

banco = sq.connect("ricardaofather.db")
cursor = banco.cursor()

def linha():
    print("-------------------------------------------------")

# 1. UPDATE – Aumentando todos os salários em 10%
# cursor.execute("UPDATE funcionarios SET salario = salario * 1.10")
# banco.commit()
# cursor.execute("SELECT salario FROM funcionarios")
# print(cursor.fetchall())

# 2. UPDATE – Alterando telefone de cpf 15967994960 para (11) 98888-7777
# cursor.execute("UPDATE funcionarios SET telefone = '(11) 98888-7777' WHERE cpf = 15967994960")
# banco.commit()
# cursor.execute("SELECT pnome,telefone,cpf FROM funcionarios WHERE cpf = 15967994960 ")
# print(cursor.fetchall())

# 3. UPDATE – Mudança de departamento Ana Athayde foi para o RH
# cursor.execute("UPDATE funcionarios SET departamento ='TI' WHERE pnome = 'Ana' AND snome = 'Athayde'")
# banco.commit()
# cursor.execute("SELECT * FROM funcionarios WHERE pnome = 'Ana' and snome = 'Athayde'")
# print(cursor.fetchall())

# 4. UPDATE – Corrigindo cargo, Um funcionário do cargo Estagiário foi promovido a Analista.
# cursor.execute("UPDATE funcionarios SET cargo ='Analista' WHERE pnome = 'Daniel' AND cargo = 'Estagiário'")
# banco.commit()
# cursor.execute("SELECT * FROM funcionarios WHERE pnome = 'Daniel' and cargo = 'Analista'")
# print(cursor.fetchall())

# 5. DELETE – Excluir por idade
# A empresa descobriu que existem registros incorretos de funcionários com idade menor que 20 anos. Remova esses registros com um DELETE.
# cursor.execute("DELETE from funcionarios WHERE idade <20")
# banco.commit()
# cursor.execute("SELECT idade, pnome FROM funcionarios")
# print(cursor.fetchall())

# 6. DELETE – Funcionário específico
# O funcionário chamado Victor pediu demissão. Escreva o comando para excluir esse funcionário do banco.
# cursor.execute("DELETE from funcionarios WHERE pnome = 'Victor' AND id = 16")
# banco.commit()
# cursor.execute("SELECT id FROM funcionarios")
# print(cursor.fetchall())

# 7. DELETE – Departamentos encerrados
# O departamento Marketing foi encerrado. Apague todos os registros de funcionários que pertencem a esse departamento.
# cursor.execute("DELETE from funcionarios WHERE departamento = 'Marketing'")
# banco.commit()
# cursor.execute("SELECT departamento FROM funcionarios")
# print(cursor.fetchall())

# BONUS !!! 👺
# 8. DELETE – CPF duplicado. Escreva um comando que apague um dos registros com o CPF repetido.
# cursor.execute("DELETE from funcionarios WHERE departamento = 'Marketing'")
# banco.commit()
