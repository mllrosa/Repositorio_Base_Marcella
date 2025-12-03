# Média com break
soma = 0
nota = 0

while True:
    nota = float(input('Digite a nota do aluno: \n ou \n Digite 99 para SAIR: '))
    if nota == 99:
        break
    soma += nota
    print(f' A média do aluno é {soma / 4}')