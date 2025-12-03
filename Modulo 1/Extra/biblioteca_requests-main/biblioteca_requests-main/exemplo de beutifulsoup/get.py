import requests

url = "https://68641b8088359a373e978349.mockapi.io/produto"

response = requests.get(url)
print(response)
print(response.json()) #status.code/headers


