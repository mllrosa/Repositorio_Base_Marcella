from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa o navegador
navegador = webdriver.Chrome()
navegador.get("https://quotes.toscrape.com")

# Pega todas as frases e autores
frases = navegador.find_elements(By.CLASS_NAME, "text")
autores = navegador.find_elements(By.CLASS_NAME, "author")

# Imprime frases e autores
for i in range(len(frases)):
    print(frases[i].text)
    print(f"- {autores[i].text}\n")

# Fecha o navegador
navegador.quit()
