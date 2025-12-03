from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/members')
def get_members():
    # Carrega os membros do arquivo JSON
    try:
        with open('members.json', 'r', encoding='utf-8') as f:
            members = json.load(f)
        return jsonify(members)
    except FileNotFoundError:
        # Retorna dados padrão se o arquivo não existir
        return jsonify([
            {
                "id": 1,
                "name": "Carlos Silva",
                "instrument": "Saxofone Tenor",
                "bio": "Com mais de 15 anos de experiência, Carlos é conhecido por seus solos improvisados que cativam o público.",
                "image": "https://images.unsplash.com/photo-1560869713-7d9aea7ebcd6?w=300&h=300&fit=crop"
            },
            {
                "id": 2,
                "name": "Ana Rodrigues", 
                "instrument": "Piano",
                "bio": "Formada no Conservatório de Música, Ana traz uma abordagem contemporânea ao jazz tradicional.",
                "image": "https://images.unsplash.com/photo-1511735111819-9a3f7709049c?w=300&h=300&fit=crop"
            }
        ])

if __name__ == '__main__':
    # Cria a pasta templates se não existir
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(debug=True, port=5000)