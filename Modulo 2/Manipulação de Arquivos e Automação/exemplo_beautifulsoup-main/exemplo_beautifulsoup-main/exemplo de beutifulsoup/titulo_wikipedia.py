# Dicas:
 
# * find_all("tag"): retorna todas as tags HTML do tipo indicado (ex: todas as <p> da página). Ele devolve uma lista.
# * find("tag"): retorna apenas a primeira ocorrência da tag indicada. Ele devolve um único elemento, não uma lista.
from bs4 import BeautifulSoup
import requests
 
# Faz a requisição da página desejada
url = "https://www.wikipedia.org/"
resposta = requests.get(url)
 
# Analisa o conteúdo HTML que foi inserido no 'resposta'
sopa = BeautifulSoup(resposta.text, "html.parser")
 
# Imprime o que tiver dentro das tags 'h1', 'p' e 'a'
print("Tags <h1>:")
for h1 in sopa.find_all("h1"):
    print(h1.text)
 
# Acha todas as Tags 'p'
"""print("\nTags <p>:")
for p in sopa.find_all("p"):
    print(p.text)
 """
 
# Acha todas as Tags 'a'
"""print("\nTags <a>:")
for a in sopa.find_all("a"):
    print(a.text)"""