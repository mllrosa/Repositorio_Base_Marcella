import requests

id = 2
url = f"https://68641b8088359a373e978349.mockapi.io/produto/{id}"

produto = {
    "marca": "Rosa",
    "tamanho": "p",
    "preço": 200.00

}

response = requests.put(url, data=produto)
print(response)