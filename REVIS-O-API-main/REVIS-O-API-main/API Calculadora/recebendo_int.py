from flask import Flask

app = Flask(__name__)

@app.route('/login/<nome>&<idade>')
def loginn(nome,idade):
        return '<h1> {}, Bem vindo ao sistema, sua idede é: {} </h1>'.format(nome, idade) # '<h1> AA {}'.format(variavel)

# 2 - Criem uma rota para Calculadora:
## SOMA
@app.route('/somar/<int:num1>&<int:num2>') 
def somar(num1,num2):
        soma = num2 + num1
        return '<h1> A soma de {} e {} é :{}'.format(num1, num2, soma)

## SUBTRAÇÃO
@app.route('/subtrair/<int:num1>&<int:num2>')
def subtrair(num1,num2):
        sub = num2 - num1
        return '<h1> A subtração de {} e {} é :{}'.format(num1, num2, sub)

## DIVISÃO
@app.route('/dividir/<int:num1>&<int:num2>')
def dividir(num1,num2):
        divi = num2 / num1
        return '<h1> A divisão de {} e {} é :{}'.format(num1, num2, divi)

## MULTIPLICAÇÃO
@app.route('/multiplicacao/<int:num1>&<int:num2>')
def multiplicacao(num1,num2):
        mult = num2 * num1
        return '<h1> A multiplicação de {} e {} é :{}'.format(num1, num2, mult)
        
if __name__ == "__main__":
    app.run(debug=True)
