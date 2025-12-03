# 🧾 PROJETO 12 — Sistema de Notas Escolares
# Crie um sistema que receba as notas de alunos e calcule a média e situação final (Aprovado/Reprovado).


# 🧾 PROJETO 12 — Sistema de Notas (Versão Simples)

def main():
    alunos = []
    
    print("📚 SISTEMA DE NOTAS")
    
    while True:
        print("\n1. Adicionar aluno")
        print("2. Ver notas")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
            
            media = (nota1 + nota2 + nota3) / 3
            situacao = "Aprovado" if media >= 7 else "Reprovado"
            
            aluno = {
                'nome': nome,
                'media': media,
                'situacao': situacao
            }
            
            alunos.append(aluno)
            print(f"Aluno {nome} cadastrado! Média: {media:.1f} - {situacao}")
            
        elif opcao == "2":
            print("\n--- NOTAS DOS ALUNOS ---")
            for aluno in alunos:
                print(f"{aluno['nome']}: Média {aluno['media']:.1f} - {aluno['situacao']}")
                
        elif opcao == "3":
            print("Até logo!")
            break
            
        else:
            print("Opção inválida!")

main()