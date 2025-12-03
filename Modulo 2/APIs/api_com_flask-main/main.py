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
def adicionar_aluno():
    novo_aluno = request.get_json()
    
    # Verificar se o id já existe
    for aluno in alunos:
        if aluno["id"] == novo_aluno["id"]:
            return jsonify({"erro": "Aluno com este ID já existe."}), 400

    alunos.append(novo_aluno)
    return jsonify({"mensagem": "Aluno adicionado com sucesso!", "aluno": novo_aluno})

# 3 FOI
@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            dados = request.get_json()
            aluno.update(dados)
            return jsonify({"mensagem": "Aluno atualizado!", "aluno": aluno})
    return jsonify({"erro": "Aluno não encontrado!"}), 404

# 4 FOI
@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_alunos(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify({"mensagem": "Aluno removido!"})
    return jsonify({"erro": "Aluno não encontrado!"}), 404


#------
if __name__ == "__main__":
    app.run(debug=True)

# corrigido