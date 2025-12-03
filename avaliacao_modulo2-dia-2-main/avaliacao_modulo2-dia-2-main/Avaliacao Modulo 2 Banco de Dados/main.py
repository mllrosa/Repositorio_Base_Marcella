import sqlite3

# 1) Criar banco de dados
banco = sqlite3.connect("escola.db")
cursor = banco.cursor()

# 2) Criar tabela alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    email TEXT
)
""")

# 3) Inserir registros
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ('MaLL', 17, 'maLL@123.com'))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ('Emily', 18, 'milly@123.com'))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ('MeLL', 19, 'mel@123.com'))
banco.commit() 

# 4) Listar todos
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())

# 5) Buscar por ID
cursor.execute("SELECT * FROM alunos WHERE id = 3")
print(cursor.fetchall())

# 6) Atualizar registros
cursor.execute("UPDATE alunos SET nome = 'Ricardo' WHERE id = 3")
banco.commit()
cursor.execute("SELECT * FROM alunos WHERE id = 3")
print(cursor.fetchall())

# 7) Deletar registros
cursor.execute("DELETE FROM alunos WHERE id = 3")
banco.commit()
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())
''
banco.close()