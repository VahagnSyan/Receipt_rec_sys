"""
Module for user authentication
"""


import os
from hashlib import sha256
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]
app = Flask(__name__)
CORS(app)


def register():
    """
    Register a new user.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")
    categories = []
    purchases = []

    if users_collection.find_one({"username": username}):
        return jsonify({"success": False, "message": "Username already exists"}), 400

    hashed_password = sha256(password.encode()).hexdigest()

    users_collection.insert_one(
        {"username": username, "password": hashed_password,
         "categories": categories, "purchases": purchases}
    )
    return jsonify({"success": True, "message": "Registration successful"}), 201


def login():
    """
    Login a user.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")

    hashed_password = sha256(password.encode()).hexdigest()

    user = users_collection.find_one({"username": username, "password": hashed_password})
    if user:
        user_id = str(user.get('_id'))
        return jsonify({"success": True, "user_id": user_id,
                        "username": username, "message": "Login successful"}), 200
    return jsonify({"success": False, "message": "Invalid username or password"}), 401


@app.route("/register", methods=["POST"])
def register_route():
    """
    Route for user registration.
    """
    return register()


@app.route("/login", methods=["POST"])
def login_route():
    """
    Route for user login.
    """
    return login()


if __name__ == "__main__":
    app.run(debug=True)
