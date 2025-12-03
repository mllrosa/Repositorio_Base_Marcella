from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
    {"id": 2, "nome":"Rosa", "sobrenome":"MaLL"},
    {"id": 3, "nome":"Milissa", "sobrenome":"Masser"}
    ]

#------
@app.route("/")
def home():
    return "API funcionando!"

# 1 FOI
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

# 2 FOI
@app.route("/alunos", methods=["POST"])
def adicionar_alunos():
    novo_alunos = request.get_json()
    alunos.append(novo_alunos)
    return jsonify({"mensagem": "aluno adicionado com sucesso!", "alunos": novo_alunos})


# 3 FOI
@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            dados = request.get_json()
            aluno.update(dados)
            return jsonify({"mensagem": "Nome atualizado!", "alunos": aluno})
    return jsonify({"erro": "alunos não encontrado!"}), 404

# 4 FOI
@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_alunos(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify({"mensagem": "alunos removido!"})
    return jsonify({"erro": "alunos não encontrado!"}), 404

#------
if __name__ == "__main__":
    app.run(debug=True)


# sem correcao de pt