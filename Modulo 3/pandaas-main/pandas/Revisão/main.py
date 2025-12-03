# SÉRIES: É uma estrutura unidimensional — parecida com uma coluna de uma tabela ou uma lista com rótulos (índices).
# Tem rótulos (index) e valores (values)

# DATAFRAME - É uma estrutura bidimensional — como uma tabela do Excel
# Cada coluna de um DataFrame é, na verdade, uma Series. Possui linhas e colunas, com índices para ambos.

import pandas as pd

# s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(s)


data = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 31]
}
df = pd.DataFrame(data)
print(df)

# https://github.com/ricardolimaa29/revis-o_pandas_modulo3/blob/main/README.md
