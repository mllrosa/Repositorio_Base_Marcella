numeros = [1, 2, 3, 4, 5]
nomes = ["Joaquim", "Maria", "Ana"]

print(numeros)
print(nomes)

print(nomes[0])
print(nomes[1])
print(nomes[2])

nomes[0] = "João" # estava Joaquim
nomes[1] = "Luana"
nomes[2] = "Melissa"

print(nomes[0])
print(nomes[1])
print(nomes[2])

nomes = ["Joaquim", "Maria", "Ana"]
nomes.append("Julia")
nomes.append("Sara")
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])


nomes.insert(1, "Fernanda") # Insere "Fernanda" na posição 1
print("Após insert:", nomes)

# Modificando elementos
nomes[2] = "Paulo" # Modifica o elemento no indice 2
print("Após modificação:", nomes)

# Removendo elementos
del nomes [3] # Remove o elemento no índice 3
print("Após del:", nomes)

nomes.remove("Fernanda") # Remove a primeira ocorrência de "Fernanda"
print("Após remove:", nomes)

removido = nomes.pop(2) # Remove e retorna o elemento no indice 2
print(f"Após pop(revovido'{removido}'):", nomes)

nomes.clear() # Esvazia a lista
print("Após clear:", nomes)