from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://books.toscrape.com/")

# Pega todos os artigos (livros)
livros = navegador.find_elements(By.CLASS_NAME, "product_pod")

for livro in livros:
    # título dentro do link do h3
    titulo = livro.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
    # preço dentro do p.price_color
    preco = livro.find_element(By.CLASS_NAME, "price_color").text
    print(f"{titulo} - {preco}")

navegador.quit()

