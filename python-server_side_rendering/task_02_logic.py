from flask import Flask, render_template
import json

app = Flask(__name__)

# Route pour la liste des items
@app.route('/items')
def items():
    # Lire les données depuis le fichier JSON
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get('items', [])  # Obtenir la liste des items ou une liste vide par défaut
    return render_template('items.html', items=items_list)

# Route d'accueil (optionnelle, si non déjà créée)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
