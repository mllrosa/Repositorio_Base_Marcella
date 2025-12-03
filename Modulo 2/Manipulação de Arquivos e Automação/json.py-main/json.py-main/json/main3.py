import json

with open("json_dados.json", "r", encoding="utf-8") as arquivo:
    biblioteca = json.load(arquivo)

print(biblioteca)
print(biblioteca["nome"])