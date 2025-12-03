# Média com while
# 'nota_total' é o acumulador de notas
nota_bimestral = 0
bimestre = 0

while bimestre < 4:
    nota = float(input('Digite a nota do aluno: '))
    nota_total += nota #Acumulando a nota total
    bimestre += 1
    print(f'A {nota} digitada do aluno foi armazenada com sucesso!')

media = nota_total / 4 # Calculando a média após sair do loop
print(f'A média do aluno é {media}')

