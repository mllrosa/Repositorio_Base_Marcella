import requests

# Exiba no console (terminal) o código de status de uma requisição GET.
url = 'http://172.25.253.124:5000/alunos'
resposta = requests.get(url)
print(resposta.status_code)

# Adicione seus dados (nome e email) utilizando o POST com o requests
dados = {'nome': 'Rosa', 
         'email': 'rosa@gmail.com'}
requests.post(url, json=dados)

# Visualize os dados submetidos através de uma requisição GET.
resposta2 = requests.get(url)
print(resposta2.json()) #json/text