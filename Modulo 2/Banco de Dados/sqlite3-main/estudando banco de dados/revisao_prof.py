import sqlite3

# Conexão com o banco
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# ============================
# 1 - CREATE: Criação das tabelas
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nacionalidade TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    ano INTEGER,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_livro INTEGER,
    nome_aluno TEXT,
    data_emprestimo TEXT,
    data_devolucao TEXT,
    FOREIGN KEY (id_livro) REFERENCES livros(id)
)
""")

# ============================
# 2 - INSERT: Inserir dados
# ============================

cursor.execute(
    "INSERT INTO autores (nome, nacionalidade) VALUES (?, ?)",
    ("Machado de Assis", "Brasileiro")
)
cursor.execute(
    "INSERT INTO livros (titulo, ano, id_autor) VALUES (?, ?, ?)",
    ("Dom Casmurro", 1899, 1)
)

# --- 
# 👉 TAREFA: Inserir mais autores e livros
cursor.execute(
    "INSERT INTO autores (nome, nacionalidade) VALUES (?, ?)",
    ("Maria", "Brasileira")
)
cursor.execute(
    "INSERT INTO autores (nome, nacionalidade) VALUES (?, ?)",
    ("Elio", "German")
)

cursor.execute(
    "INSERT INTO livros (titulo, ano, id_autor) VALUES (?, ?, ?)",
    ("Divergentes", "2007", "4")
)
cursor.execute(
    "INSERT INTO livros (titulo, ano, id_autor) VALUES (?, ?, ?)",
    ("Convergentes", "2008", "4")
)

# ============================
# 3 - UPDATE: Atualizar a data de devolução de um livro
# ============================

# 👉 COMPLETE:
cursor.execute(
    "INSERT INTO emprestimos (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
    (1, "Luís", "12/11/2020", "20/11/2020")
)
cursor.execute(
    "INSERT INTO emprestimos (id_livro, nome_aluno, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
    (2, "Rosa", "19/09/2020", "21/09/2020")
)

cursor.execute(
    "UPDATE emprestimos SET data_devolucao = '11/12/2999' WHERE id = 1"
)

# cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", ("11/12/2989", 1))  # DEU ERRO

# ============================
# 4 - SELECT: Consultar os livros emprestados por um aluno
# ============================

# 👉 COMPLETE:
cursor.execute(
    "SELECT * FROM emprestimos WHERE nome_aluno = 'Rosa'"
)
print(cursor.fetchall())

# ============================
# 5 - DELETE: Remover um empréstimo concluído
# ============================

# 👉 COMPLETE:
cursor.execute("DELETE FROM emprestimos WHERE id = 1")

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()
