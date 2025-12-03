import requests

url = 'http://172.25.253.124:5000/deletar_alunos'
# response = requests.delete(url ,{id= 8})
id = input(int("id:"))
url = f"http://deletaralunos/{id}"
requisicao = requests.delete(f"{url}/{id}")
print(requisicao.status_code)

