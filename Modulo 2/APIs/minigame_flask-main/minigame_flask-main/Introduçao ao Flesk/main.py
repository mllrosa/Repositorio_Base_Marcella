from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# tela de inicio, tem pede o nome
from route import *

# ja é pra ter o minigame nesse
from route1 import *

if __name__ == "__main__":
    app.run(debug=True)