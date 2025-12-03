
# 1- O BANCO QUE CRIAMOS EM SALA DE AULA, É UM BANCO RELATIVO?
import sqlite3 as sq

# 2- CRIE UM BANCO DE DADOS DE UMA loja
banco = sq.connect("dados_loja.db")
cursor = banco.cursor()

# 3- COLOQUE AO MENOS 5 COLUNAS
cursor.execute("CREATE TABLE produtos (marca text, validade integer, fornecedor text, quantidade_comp text, preço integer)")

# 4- INSIRA VALORES DENTRO DESSES CAMPOS ()
cursor.execute("INSERT INTO produtos VALUES ('Tylenol', 202609, 'Farmadistribuidora Ltda', '20 comprimidos', 12.50)")
cursor.execute("INSERT INTO produtos VALUES ('Neosaldina', 202507, 'Pharma Brasil Distrib.', '30 comprimidos', 18.90)")
cursor.execute("INSERT INTO produtos VALUES ('Dipirona Genérico', 202604, 'Genfarma SA', '1 frasco de 100 ml', 6.75)")
cursor.execute("INSERT INTO produtos VALUES ('Amoxicilina', 202511, 'Biotec Pharma', '21 cápsulas', 25.00)")
cursor.execute("INSERT INTO produtos VALUES ('Ibuprofeno', 202603, 'MedExpress Distribuidora', '10 comprimidos', 9.30)")
banco.commit()

# 5- MOSTRE OS VALORES NO TERMINAL E NO SQLITE VIEWER
cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())

