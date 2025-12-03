from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://books.toscrape.com/")

#b = navegador.find_elements(By.CLASS_NAME, "price_color")

preco = navegador.find_element(By.CSS_SELECTOR , "product_price h3 a")
titulos = navegador.find_element(By.CSS_SELECTOR, "")


for i in range(len(titulos)):
    print(titulos[i].text)
    print(f"- {preco[i].text}")
    print()