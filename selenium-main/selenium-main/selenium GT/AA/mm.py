import os
import csv
import requests
from bs4 import BeautifulSoup
import pyautogui

# 1. Criar pasta 'relatorios' se não existir
pasta = "relatorios"
if not os.path.exists(pasta):
    os.mkdir(pasta)
print("Pastas atuais:", os.listdir())

# 2. Coletar título do site (título da página)
url = 'https://books.toscrape.com'
resposta = requests.get(url)
site = BeautifulSoup(resposta.text, "html.parser")

titulo = site.title.text if site.title else "Título não encontrado"
print("Título do site:", titulo)

# 3. Salvar em CSV dentro da pasta 'relatorios'
caminho_arquivo = os.path.join(pasta, "livros.csv")
with open(caminho_arquivo, "w", newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["Título do Site de Livros"])
    escritor.writerow([titulo])

# 4. Ler do CSV e "enviar para formulário" (aqui só printa)
with open(caminho_arquivo, "r", encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)  # pular cabeçalho
    for linha in leitor:
        if linha:
            titulo_livro = linha[0]
            print("Enviando para formulário:", titulo_livro)

# 5. Aviso com pyautogui
pyautogui.alert(text=f"Título do site: {titulo}", title="Aviso", button="OK")
