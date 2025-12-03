import json

dados = {
  "nome": "João",
  "idade": 30,
  "cidade": "São Paulo"
}

dadospy = json.loads(dados)

print(dados["nome"])

