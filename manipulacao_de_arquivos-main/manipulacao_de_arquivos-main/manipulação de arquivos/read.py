arquivo = open('arquivo.txt', 'r', encoding = 'utf-8')
# Read the entire file
conteudo = arquivo.read()
# Imprimir o conteúdo do arquivo
print(conteudo)
arquivo.close()
