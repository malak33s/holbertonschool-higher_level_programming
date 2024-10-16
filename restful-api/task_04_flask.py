#!/usr/bin/python3
"""
Une simple API Flask pour gérer des utilisateurs.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}

@app.route("/")
def home():
    """Message de bienvenue."""
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """Retourne la liste des noms d'utilisateur."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Retourne l'état de l'API."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Retourne les informations d'un utilisateur."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Ajoute un nouvel utilisateur."""
    user_data = request.get_json()
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run()

