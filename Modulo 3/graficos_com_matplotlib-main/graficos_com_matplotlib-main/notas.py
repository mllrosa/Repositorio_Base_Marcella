import matplotlib.pyplot as plt

# As notas das suas últimas provas

notas = [30, 18, 24, 30]
materias = ("Sociologia", "Inglês", "História", "Matemática")

plt.bar(materias, notas)
plt.title("Notas")
plt.show()