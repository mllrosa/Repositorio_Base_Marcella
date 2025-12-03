import os
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

# 1. Criar pasta
import os

# os.mkdir("Projetos")
# os.rename("Projetos", "Relatorios")
print("Pastas:", os.listdir())

# 2. Coletar título do site
import requests
from bs4 import BeautifulSoup

resposta = requests.get('https://books.toscrape.com&quot')
site = BeautifulSoup(resposta.text, "html.parser")
titulo = site.find("h1").text

print("Título do site:", titulo)

# 3. Salvar em CSV
with open("Relatorios/livros.csv", "w", newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["Título do Site de Livros"])
    escritor.writerow([titulo])

# 4. Ler do CSV e enviar para formulário
with open("Relatorios/livros.csv", "r", encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        titulo_livro = linha[0]
        print("Enviando para formulário:", titulo_livro)

# 5. Aviso com pyautogui
pyautogui.alert(text=f"Título do site: {titulo}", title="Aviso", button="OK")