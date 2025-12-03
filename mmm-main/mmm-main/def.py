# usando def para definir algumas funções 

def buscar_informacao(nome):
    informacoes = {
        "rosa": "numero 1",
        "amarelo": "numero 2",
        "vermelho": "numero 3"
    }
    
    return informacoes.get(nome.lower(), "Informação não encontrada.")
#lower transforma as letras em letras minúsculas pra evitar erros de busca devido a digitação 
# ---


def buscar_informacao(nome):
    a = a.lower()  # transforma aqui em vez de no return
    informacoes = {
        "rosa": "primeira",
        "amarelo": "segunda",
        "vermelho": "terceira"
    }
    return informacoes.get(nome, "Informação não encontrada.")

"""
if nome in informacoes:
    return informacoes[nome]
else:
    return "Informação não encontrada.
"""
#---

#exemplo com cotação de moedas 

def cotacao(moeda):
    moeda = moeda.lower()
    match moeda:
        case "dolar":
            return 5.35
        case "euro":
            return 5.80
        case "iene":
            return 0.038
        case _:
            return "Moeda não encontrada."
