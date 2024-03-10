from flask import Flask, request, jsonify
from pymongo import MongoClient
from hashlib import sha256
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Check if the username already exists
    if users_collection.find_one({"username": username}):
        return jsonify({"success": False, "message": "Username already exists"}), 400

    # Hash the password before storing it
    hashed_password = sha256(password.encode()).hexdigest()

    # Insert the user into the database
    users_collection.insert_one({"username": username, "password": hashed_password})
    return jsonify({"success": True, "message": "Registration successful"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Hash the password to match with the stored hash
    hashed_password = sha256(password.encode()).hexdigest()

    # Check if the username and hashed password match
    user = users_collection.find_one({"username": username, "password": hashed_password})
    if user:
        return jsonify({"success": True, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)
