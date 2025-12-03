"""
Pegar Informações - GET
Criar Informações - POST
Editar Informações - PATCH
Deletar Informações - DELETE
"""
#GET
import requests
requisicao = requests.get("")
print(requisicao) #resposta 200
print(requisicao.json()) #pegar a informação armazenada dentro da requisição

#POST
import requests
url = ""
dados = {"nome": "Rosa", "idade": 17}
requisicao = requests.post(url, json=dados)
print(requisicao) # resposta 200
print(requisicao.json()) # resposta do servidor

#PUT/PATCH
#atualiza tudo put
import requests
id = 3
url = f"ejjshsvjs/{id}"
dados = {"nome": "Rosaa Atualizada", "idade": 18}
requisicao = requests.put(url, json=dados)
print(requisicao)             
print(requisicao.json())

#atualiza parcialmente patch
import requests
id = 1
url = f"ejjshsvjs/{id}"
dados = {"idade": 19}  # Só atualiza a idade
requisicao = requests.patch(url, json=dados)
print(requisicao)
print(requisicao.json())

#DELETE
import requests
id = 3
url = f"ejjshsvjs/{id}"
requisicao = requests.delete(url)
print(requisicao)
print(requisicao.status_code)

"""
INFORMAÇÃO NO FORMATO JSON
{
  "nome": "João",
  "idade": 30,
  "cidade": "São Paulo"
}

"""