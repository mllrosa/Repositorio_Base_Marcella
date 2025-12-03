
import sqlite3 as sq

banco = sq.connect("dados_loja.db")
cursor = banco.cursor()

# ('Neosaldina', 202507, 'Pharma Brasil Distrib.', '30 comprimidos', 18.90)
cursor.execute("UPDATE produtos SET validade = 282808 WHERE validade = 202507")
# ('Ibuprofeno', 202603, 'MedExpress Distribuidora', '10 comprimidos', 9.30)
cursor.execute("UPDATE produtos SET marca = 'rosa', fornecedor = 'rosa' WHERE validade = 202603")
banco.commit()

cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())
banco.close()