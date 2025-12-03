# 1. Importe 'pandas' como pd
import pandas as pd

# 2. Transforme o dicionário em um DataFrame e exiba a tabela Dataframe
funcionarios = {
    "nome": [
        "Ana Souza", "Bruno Lima", "Carla Ferreira", "Diego Santos", "Eduarda Nascimento",
        "Felipe Almeida", "Giovana Ramos", "Henrique Costa", "Isabela Araujo", "João Pereira",
        "Karina Oliveira", "Lucas Rodrigues", "Mariana Machado", "Nathan Silva", "Olívia Barbosa"
    ],
    "unidade": [
        2, 1, 3, 2, 1,
        3, 1, 2, 3, 1,
        2, 3, 1, 3, 2
    ],
    "escala_noturna": [
        False, True, False, True, False,
        True, False, True, False, True,
        False, True, False, True, False
    ],
    "vendas": [
        18754.32, 24321.89, 19876.45, 27543.22, 15789.66,
        29123.10, 22345.99, 26789.40, 19456.78, 28345.55,
        17654.12, 23876.99, 20543.70, 29654.88, 18321.44
    ]
}

df = pd.DataFrame(funcionarios)
print(df)
#  ---

import pandas as pd

# 3. Exiba as informacoes de dimencoes, linha, colunas e tipos de dados do DataFrame

df['nome']

df.head(1)
#  ---

import pandas as pd

# 4. Quantos funcionarios temos em cada unidade?

df['unidade'].value_counts()
#  ---

# 5. Seguindo a mesma logica do exercicio anterior, quantos funcionarios trabalham de noite?

df['escala_noturna'].value_counts()
#  ---

# 6. Qual foi o total de vendas do funcionario chamado Henrique Costa?

df[df['nome'] == 'Henrique Costa']['vendas']
#  ---

# 7. Quais funcionarios venderam menos do que R$ 20000?

df[df['vendas'] < 20000]
#  ---

# 8. O total de vendas é maior durante o dia ou noite?
import pandas as pd


df[df['escala_noturna'] == True]['vendas'].sum()

df[df['escala_noturna'] == False]['vendas'].sum()


# df[['vendas'] == 'False'].sum()
