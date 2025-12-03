import os
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


nome_arquivo = "data.csv"

# 1. Criar pasta
os.mkdir("Relatórios")


# 2. Coletar título do site
url = "https://books.toscrape.com"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.text, "html.parser")
print("Tags <a>:")
for a in sopa.find("a"):
    titulo_site = (a.text)


# 3. Salvar em CSV
with open(nome_arquivo, 'w', newline="") as arquivo:
    escritor = csv.writer(arquivo, delimiter=",", lineterminator="\n")
    escritor.writerow([titulo_site])


# 4. Ler do CSV e enviar para formulário
data = open("data.csv")
dados = csv.reader(data)
for linha in dados:
    print(linha)


navegador = webdriver.Chrome()
navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSe1kM6GuDUR34BcH88YdKuiCcjCQVevFWhElbNLtsoBHGob2A/viewform")


# 5. Aviso com pyautogui

pyautogui.write('Concluido!', interval = 0.2)
pyautogui.sleep(1)