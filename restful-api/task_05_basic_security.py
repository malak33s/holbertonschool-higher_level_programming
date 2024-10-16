#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration de la clé secrète pour JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change cette clé par une clé secrète forte
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Liste d'utilisateurs avec mots de passe hachés et rôles
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Fonction de vérification des utilisateurs pour l'authentification de base
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return users[username]

# Route protégée par authentification de base
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Route de connexion pour générer un token JWT
@app.route("/login", methods=["POST"])
def login():
    """Connexion et génération de JWT"""
    user_data = request.get_json()
    username = user_data.get("username")
    password = user_data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Route protégée par token JWT
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Route protégée par rôle
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Accès limité aux admins seulement"""
    current_user = get_jwt_identity()  # Récupère l'identité de l'utilisateur
    user_role = users[current_user]["role"]
    
    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Gestion des erreurs de JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run()
