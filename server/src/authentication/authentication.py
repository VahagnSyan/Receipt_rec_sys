"""
Module for user authentication
"""


import os
from hashlib import sha256
from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
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


@auth_bp.route("/login", methods=["POST"])
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
        user_id = str(user.get("_id"))
        return jsonify({"success": True, "user_id": user_id, "username": username, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401
