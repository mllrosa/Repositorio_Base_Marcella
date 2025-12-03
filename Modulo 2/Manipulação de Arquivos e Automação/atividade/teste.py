import os
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import bs4

#navegador = webdriver.Chrome()
#navegador.get("https://books.toscrape.com")




#resposta_html = requests.get("https://books.toscrape.com")
#conteudo_html = bs4(resposta_html.text, )

"""navegador = webdriver.Chrome()
navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSe1kM6GuDUR34BcH88YdKuiCcjCQVevFWhElbNLtsoBHGob2A/viewform")"""


"""# 2. Coletar título do site
navegador = webdriver.Chrome()
navegador = requests.get("https://books.toscrape.com")
frases = navegador.find_elements(By.)"""

from bs4 import BeautifulSoup
import requests
 

url = "https://books.toscrape.com"
resposta = requests.get(url)
 
sopa = BeautifulSoup(resposta.text, "html.parser")

print("Tags <a>:")

for a in sopa.find("a"):
    print(a.text)