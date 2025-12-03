import os

os.mkdir("matematica.txt")
os.mkdir("portugues.txt")
os.mkdir("ciencias.txt")

arquivos = os.listdir()
for item in arquivos:
    print(item)

os.rename("ciencias.txt", "historia.txt")

if os.path.exists("projetos/matematica.txt"):
    os.remove("matematica.txt")
    print("Arquivo apagado")
else:
    print("Arquivo não encontrado")







input("apagar?")

arquivos = os.listdir()
print(arquivos)

for item  in arquivos:
    if item == "main.py"
    pass
os.rmdir(item)