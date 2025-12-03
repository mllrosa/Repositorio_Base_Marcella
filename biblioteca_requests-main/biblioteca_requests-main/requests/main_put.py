import requests

id = 2
url = 'http://172.25.253.124:5000/put_alunos'

dados = {'nome': 'Rosa', 
         'email': 'rosa@gmail.com'}

requisicao = requests.put(f"{url}/{id}", json=dados)


print(requisicao.status_code)

