
# -- 📝 Cria tabelas    --------------------------------------------
# -- id, polo, preco, data_matricula, situacao
CREATE TABLE matriculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    polo TEXT NOT NULL,
    preco INTEGER NOT NULL,
    data_matricula DATE NOT NULL,
    situacao TEXT NOT NULL
);

# -- id, nome_curso, carga_horaria, sala, educador, nivel
CREATE TABLE cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    nome_curso TEXT NOT NULL,
    carga_horaria INTEGER NOT NULL,
    sala TEXT NOT NULL,
    educador TEXT NOT NULL,
    nivel TEXT NOT NULL
);


# -- 📝 Inserção de Dados    ------------------------------------------
# -- MATRICULAS - id, polo, curso, preco, data_matricula, situacao
INSERT INTO matriculas (polo, preco, data_matricula, situacao) VALUES
('Rosa', 2500, '15/01/2024', 'ativa'),
('Girassol', 1800, '10/02/2024', 'concluída'),
('Tulipa', 2200, '20/01/2024', 'ativa'),
('Rosa', 1500, '05/03/2024', 'ativa'),
('Girassol', 2500, '30/01/2024', 'cancelada'),
('Tulipa', 1800, '25/02/2024', 'concluída'),
('Rosa', 2200, '12/02/2024', 'ativa'),
('Girassol', 1500, '15/03/2024', 'ativa'),
('Tulipa', 2500, '18/01/2024', 'concluída'),
('Rosa', 1800, '22/02/2024', 'ativa'),
('Girassol', 2200, '01/03/2024', 'ativa'),
('Tulipa', 1500, '25/01/2024', 'concluída'),
('Rosa', 2500, '10/02/2024', 'ativa'),
('Girassol', 1800, '07/03/2024', 'ativa'),
('Tulipa', 2200, '05/01/2024', 'concluída'),
('Rosa', 1500, '14/02/2024', 'ativa'),
('Girassol', 2500, '09/03/2024', 'concluída'),
('Tulipa', 1800, '03/01/2024', 'ativa'),
('Rosa', 2200, '28/02/2024', 'ativa'),
('Girassol', 1500, '17/01/2024', 'concluída'),
('Tulipa', 2500, '21/02/2024', 'ativa'),
('Rosa', 1800, '11/03/2024', 'ativa'),
('Girassol', 2200, '19/01/2024', 'concluída'),
('Tulipa', 1500, '27/02/2024', 'ativa'),
('Rosa', 2500, '15/03/2024', 'ativa'),
('Girassol', 1800, '05/01/2024', 'concluída'),
('Tulipa', 2200, '23/02/2024', 'ativa'),
('Rosa', 1500, '02/03/2024', 'ativa'),
('Girassol', 2500, '26/01/2024', 'concluída'),
('Tulipa', 1800, '14/02/2024', 'ativa');


# -- CURSOS - id, nome_curso, carga_horaria, sala, educador, nivel
INSERT INTO cursos (nome_curso, carga_horaria, sala, educador, nivel) VALUES
('Desenvolvimento Web', 80, 'Sala 101', 'Ana Lima', 'Intermediário'),
('Ciência de Dados', 45, 'Sala 102', 'Carlos Souza', 'Iniciante'),
('Segurança da Informação', 60, 'Sala 103', 'Fernanda Alves', 'Avançado'),
('Inteligência Artificial', 20, 'Sala 104', 'Juliano Ribeiro', 'Intermediário'),
('Desenvolvimento Mobile', 80, 'Sala 105', 'Marina Duarte', 'Intermediário'),
('Big Data', 45, 'Sala 106', 'João Pedro', 'Avançado'),
('Redes de Computadores', 60, 'Sala 107', 'Patrícia Gomes', 'Iniciante'),
('Machine Learning', 20, 'Sala 108', 'Rodrigo Lima', 'Avançado'),
('DevOps', 80, 'Sala 109', 'Lucas Barros', 'Intermediário'),
('Banco de Dados', 45, 'Sala 110', 'Carla Mendes', 'Iniciante'),
('Cloud Computing', 60, 'Sala 111', 'Rafael Torres', 'Avançado'),
('Automação de Testes', 20, 'Sala 112', 'Bianca Freitas', 'Intermediário'),
('Front-end Avançado', 80, 'Sala 113', 'André Martins', 'Avançado'),
('Back-end com Node.js', 45, 'Sala 114', 'Sérgio Antunes', 'Intermediário'),
('Programação Orientada a Objetos', 60, 'Sala 115', 'Juliana Mota', 'Iniciante'),
('Scrum e Ágil', 20, 'Sala 116', 'Pedro Henrique', 'Iniciante'),
('UX/UI Design', 80, 'Sala 117', 'Isabela Ferreira', 'Intermediário'),
('Python para Data Science', 45, 'Sala 118', 'Natalia Campos', 'Avançado'),
('Kotlin para Android', 60, 'Sala 119', 'Marcelo Araújo', 'Intermediário'),
('Segurança em Redes', 20, 'Sala 120', 'Renata Lima', 'Avançado'),
('Angular e TypeScript', 80, 'Sala 121', 'Eduardo Costa', 'Intermediário'),
('Testes Automatizados', 45, 'Sala 122', 'Larissa Nunes', 'Iniciante'),
('Administração de Sistemas Linux', 60, 'Sala 123', 'Daniel Lopes', 'Avançado'),
('Inteligência Artificial Avançada', 20, 'Sala 124', 'Aline Moraes', 'Avançado'),
('React.js', 80, 'Sala 125', 'Gabriel Teixeira', 'Intermediário'),
('SQL Avançado', 45, 'Sala 126', 'Amanda Rocha', 'Iniciante'),
('Arquitetura de Computadores', 60, 'Sala 127', 'Bruno Nascimento', 'Avançado'),
('Power BI para Negócios', 20, 'Sala 128', 'Tatiane Farias', 'Intermediário'),
('Flutter para Mobile', 80, 'Sala 129', 'Vitor Ribeiro', 'Intermediário'),
('Python Intermediário', 45, 'Sala 130', 'Aline Moraes', 'Intermediário');


# -- AA ----------------------------------------------------------------------------------
# -- Para adicionar somente uma coluna na tabela
ALTER TABLE cursos ADD COLUMN preco REAL;

# -- Depois pra prencher só uma coluna  com valores aleatorios de 800 à 1600
UPDATE cursos SET preco = ABS(RANDOM() % 801) + 800; # ABS = valor absoluto

# -- Para mudar só uma linha de uma culona é necessario especificar com WHERE
UPDATE cursos SET preco = ABS(RANDOM() % 801) + 800 WHERE preco IS NULL OR preco IS  0;
# o IS pode ser substituido por =

# Para deixar em tres situacoes especificas como a dos polos/ nao deu certo :(
UPDATE matriculas SET polo = RANDOM('Rosa', 'Tulipa', 'Girasol');
# -----------------------------------------------------------------------------------------





# ----------------------------------------
# -- 🔍 Etapa 3 - Consultas com SELECT
# -- Listar todos os cursos com carga horária maior que 40 horas, ordenados pela carga horária
SELECT nome_curso, carga_horaria FROM cursos WHERE carga_horaria > 40 ORDER BY carga_horaria;

# -- Mostrar os alunos e os cursos em que estão matriculados (JOIN).
# -- Mostrar a quantidade de alunos matriculados em cada curso.



# ----------------------------------------
# -- ✏️ Etapa 4 - UPDATE
# -- Aumentar em 10% o preço dos cursos com mais de 80 horas.
UPDATE cursos SET preco = preco * 1.1 WHERE carga_horaria > 80;

# -- Atualizar a cidade do professor "João da Silva" para "Rio de Janeiro"




# ----------------------------------------
# -- 🗑️ Etapa 5 - DELETE
# -- Apagar o aluno de id = 15 (e suas matrículas).
# -- Remover todos os cursos com preço menor que R$200,00
DELETE FROM cursos WHERE preco < 200; # Nao precisa  do * na vdd da erro se colocar 



# ----------------------------------------
# -- ✏️ Etapa 6 - INSERT Extra
# -- Inserir um novo curso chamado "Inteligência Artificial", 60 horas, R$1200.
INSERT INTO cursos (nome_curso, carga_horaria, sala, educador, nivel) VALUES
('Inteligência Artificial', 60, 'Sala 101', 'Ana Lima', 'Intermediário', 1000);



# ----------------------------------------
# -- 📊 Etapa 7 - Relatório Final
# -- Liste os 5 cursos mais caros e mostre quantos alunos estão matriculados em cada um:






































# -- mostrar, para cada curso, o preço do curso e os preços das matrículas associadas (JOIN).

