import requests

url = "https://68641b8088359a373e978349.mockapi.io/produto"

produto = {
    "marca": "Rosa",
    "tamanho": "p",
    "preço": 200.00

}

nova_marca = requests.post(url, json=produto)
