# Situação: Um banco de dados cinema.db já possui a tabela filmes com os campos: id, titulo, genero, ano, avaliacao


def linha():
    print('-'*30)

import sqlite3 as sq
banco = sq.connect("AA/cinema.db")
cursor = banco.cursor()

# Liste apenas os títulos e gêneros de todos os filmes.
cursor.execute("SELECT titulo, genero FROM filmes")
print(cursor.fetchall())
linha()

# Mostre todos os dados do filme cujo titulo seja "Matrix".
cursor.execute("SELECT * FROM filmes WHERE titulo = 'Matrix'")
print(cursor.fetchall())
linha()

# Exiba os títulos e avaliações de todos os filmes lançados após 2010.
cursor.execute("SELECT titulo, avaliacao FROM filmes WHERE ano > 2010")
print(cursor.fetchall())
linha()