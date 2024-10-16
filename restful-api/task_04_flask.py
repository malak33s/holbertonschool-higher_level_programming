#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    return "OK"


@app.route("/add_user", methods=["POST"])
def addUser():
    user_data = request.get_json()
    username = user_data.get("username")

    if username is None:
        return jsonify({"error": "Username is required"}), 400

    users[username] = user_data

    return jsonify(message="User added", user=user_data), 201


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
