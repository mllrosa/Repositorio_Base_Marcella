import os

os.mkdir("maatematica.txt")
os.mkdir("poortugues.txt")
os.mkdir("ciiencias.txt")

arquivos = os.listdir()
for item in arquivos:
    print(item)

# os.rename("ciiencias.txt", "hiistoria.txt")


# if os.path.exists("projetos/matematica.txt"):
#     os.remove("matematica.txt")
#     print("Arquivo apagado")
# else:
#     print("Arquivo não encontrado")


# os.removedirs()

apagar = input("AA:")


arquivos = os.listdir()
print(arquivos)

for item in arquivos:
    if item == "main.py":
        print("achouuuuuu")
        continue
    else:
        try:
            os.rmdir(item)
        except:
            os.remove(item)

# os.rmdir("matematica.txt")
# os.mkdir("portugues.txt")
# os.mkdir("ciencias.txt")