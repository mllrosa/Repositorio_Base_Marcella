import json

json_dados = {
  "nome": "João",
  "idade": 30,
  "cidade": "São Paulo"
}
#with open("json_dados.json", "w", encoding="utf-8") as arquivo:
with open ("json_dados", "w", encoding="utf-8") as arquivo:
    json.dump(json_dados, arquivo, ensure_ascii=False,indent=4)