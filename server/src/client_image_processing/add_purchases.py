"""
Module for managing user purchases
"""


import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId


load_dotenv()
client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]
app = Flask(__name__)
CORS(app)


def add_purchases():
    """
    Add purchases for a user.

    Request JSON structure:
    [
        {
            "id": "<user_id>",
            "products": [
                {
                    "name": "<product_name>",
                    "price": "<product_price>",
                    "category": "<product_category>"
                },
                ...
            ]
        }
    ]

    Returns:
        JSON response indicating success or error.
    """
    try:
        data = request.json[0].get("products")
        if not isinstance(data, list):
            return jsonify({"error": "Data should be a list of dictionaries"}), 400
        user_id = request.json[0].get("id")
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
        # products_categories = [d["category"] for d in data]
        products_categories = []
        for item in data:
            for category in item["products"].get("category"):
                products_categories.append(category)
        for item in products_categories:
            if item not in categories:
                categories.append(item)
        users_collection.update_one({"_id": object_id}, {"$set": {"purchases": purchases}})
        users_collection.update_one({"_id": object_id}, {"$set": {"categories": categories}})
        return jsonify({"message": "Data added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add", methods=["POST"])
def add_purchases_route():
    """
    Route for adding purchases.
    """
    return add_purchases()


if __name__ == "__main__":
    app.run(debug=True)
