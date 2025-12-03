import requests

id = 33
url = f"https://68641b8088359a373e978349.mockapi.io/produto/{id}"

response = requests.delete(url)
print(response)

"""
for id in range(1, 3):
    resposta = requests.delete(f"gjihuhçg/{id}")

"""