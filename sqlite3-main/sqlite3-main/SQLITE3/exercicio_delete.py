
import sqlite3 as sq
try:

    banco = sq.connect("dados_loja.db")
    cursor = banco.cursor()

    # ('Tylenol', 202609, 'Farmadistribuidora Ltda', '20 comprimidos', 12.50)
    cursor.execute("DELETE from produtos WHERE marca = 'Tylenol'")
    banco.commit()
    banco.close()
    print("Dados removidos!")

except sq.Error as erro:
    print("Erro ao Excluir:",erro)
cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())

