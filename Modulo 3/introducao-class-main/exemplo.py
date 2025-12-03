class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.notas = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota {nota} adicionada!")
    
    def calcular_media(self):
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            return media
        return 0
    
    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}")
        print(f"Tenho {self.idade} anos")
        print(f"Estou no {self.serie}º ano")
        print(f"Minha média é {self.calcular_media():.1f}")

# Usando a classe
aluno1 = Aluno("Beatriz", 15, 9)
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(9.0)
aluno1.adicionar_nota(7.5)
aluno1.apresentar()