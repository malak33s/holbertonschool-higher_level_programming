import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Fonction pour lire les données JSON
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Fonction pour lire les données CSV
def read_csv():
    products = []
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return None

# Fonction pour lire les données depuis la base de données SQLite
def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        products = cursor.fetchall()
        conn.close()
        return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]
    except sqlite3.Error as e:
        return None

# Route principale pour afficher les produits
@app.route('/products')
def products():
    # Récupérer les paramètres de la requête
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Lire les données en fonction de la source
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Gérer le cas où les données ne sont pas disponibles
    if not products:
        return render_template('product_display.html', error="No products found")

    # Filtrer par ID si un ID est fourni
    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    # Renvoyer les produits au modèle
    return render_template('product_display.html', products=products)

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5000)
