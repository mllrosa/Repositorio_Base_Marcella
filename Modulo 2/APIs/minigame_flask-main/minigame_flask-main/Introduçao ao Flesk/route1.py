from main import app
from flask import Flask, render_template, request, redirect, url_for

# Crie uma rota para processar o formulário
@app.route("/jogo", methods=["POST"])
def iniciar_jogo():
    nome_jogador = request.form["nome"]

    return f"Olá, {nome_jogador}! Bem-vindo(a) ao jogo."