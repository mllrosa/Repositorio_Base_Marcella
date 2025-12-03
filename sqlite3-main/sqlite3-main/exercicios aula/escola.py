# Existe um banco de dados escola.db com a tabela alunos contendo os campos: id, nome, idade, nota, turma
def linha():
    print('-'*30)

import sqlite3 as sq
banco = sq.connect("escola.db")
cursor = banco.cursor()

# Liste o nome e a nota de todos os alunos.
cursor.execute("SELECT nome,nota FROM alunos")
print(cursor.fetchall())
linha()

# Selecione apenas o aluno cujo id = 3.
cursor.execute("SELECT * FROM alunos WHERE id = 3")
print(cursor.fetchall())
linha()

# Exiba os alunos da turma "B" que têm nota maior ou igual a 7.
cursor.execute("SELECT * FROM alunos WHERE turma = 'B' and nota >= 7")
print(cursor.fetchall())
linha()