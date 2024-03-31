"""
Module for managing user purchases
"""


import os
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from flask_cors import CORS
from dotenv import load_dotenv
from bson import ObjectId


load_dotenv()
client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]

add_bp = Blueprint("add", __name__)


@add_bp.route("/add", methods=["POST"])
def add_purchases():
    try:
        data = request.json.get("products")
        if not isinstance(data, list):
            return jsonify({"error": "Data should be a list of dictionaries"}), 400
        user_id = request.json.get("id")
        if not user_id:
            return jsonify({"error": "User ID not provided"}), 400
        object_id = ObjectId(user_id)
        user = users_collection.find_one({"_id": object_id})
        if not user:
            return jsonify({"error": "User not found"}), 404
        purchases = user.get("purchases", [])
        for item in data:
            for purchase in item.get("products"):
                purchases.append(purchase)
        categories = user.get("categories", [])
        products_categories = []
        for item in data:
            for category in item.get("products"):
                products_categories.append(category.get("category"))
        for item in products_categories:
            if item not in categories:
                categories.append(item)
        users_collection.update_one({"_id": object_id}, {"$set": {"purchases": purchases}})
        users_collection.update_one({"_id": object_id}, {"$set": {"categories": categories}})
        return jsonify({"message": "Data added successfully"}), 200
    except Exception as e:
        return jsonify({"error": e}), 500
