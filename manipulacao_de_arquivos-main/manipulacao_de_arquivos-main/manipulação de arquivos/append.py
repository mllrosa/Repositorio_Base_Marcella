arquivo = open('arquivo.txt', 'a', encoding = 'utf-8')
# Append new lines to the file - Adiciona novas linhas no arquivo?
arquivo.write('Adicionando uma nova linha ao arquivo. \n')
arquivo.write('Está é uma linha adicional. \n')
# Close the file - Fecha arquivo
arquivo.close()