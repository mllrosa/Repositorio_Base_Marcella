import requests, bs4

res = requests.get('https://books.toscrape.com/')

soup = bs4.BeautifulSoup(res.text, "html.parser")
type(soup)

soup.title.string #carrega o titulo da pagina

titulos_livros = [] # lista para armazenar os titulos do livros

# Itera sobre c ada livro encontrado???
for livro in soup.select('.product_pod'):
    h3 = livro.find('h3')
    # verifica se o h3 nao possui atributo 'class'
    if not h3.has_attr('class'):
        titulo = h3.a['title']
        titulos_livros.append(titulo)

print(soup.title.string) #carrega o titulo da pagina
print(titulos_livros) #exibe os titulos dos livros

response = requests.get("https://books.toscrape.com/")
print(response) 
if response.status_code == 200:
    print('Conexão realizada')
else:
    print(f'Erro na conexão com servidor: {response.status_code}')
