import sqlite3 as sq

# Criamos a conexao com o banco e guardamos na variavel 'banco
banco = sq.connect("banco.db")

# Criamos a variavel cursor e colocamos em uma variavel
cursor = banco.cursor()

# Criando a tabela 'pessoas' com  os campos necessarios
cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# Inserindo na tabela desejada os valores
cursor.execute("INSERT INTO pessoas VALUES ('Santana',50,'santan@gamil.com')")

# Enviando os dados 
banco.commit()

# Printar a info
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())