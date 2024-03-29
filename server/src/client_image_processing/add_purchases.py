from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from flask_cors import CORS
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

# Connect to MongoDB
client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]


app = Flask(__name__)
CORS(app)


@app.route("/add", methods=["POST"])
def add_purchases():
    try:
        data = request.json[0].get("products")  # Get JSON data from the request
        if isinstance(data, list):  # Check if data is a list
            user_id = request.json[0].get("id")  # Retrieve the usaer ID from the request
            if user_id:  # Check if the user ID is provided
                # Find the user by their ID
                object_id = ObjectId(user_id)
                user = users_collection.find_one()
                if user:  # Check if the user is found
                    # Add purchases to the user's purchases dictionary
                    purchases = user.get("purchases", [])
                    for item in data:
                        purchases.append(item)
                    # Update the user document with the updated purchases dictionary
                    categories = user.get("categories", [])
                    products_categories = [d["category"] for d in data]
                    for item in products_categories:
                        if item not in categories:
                            categories.append(item)
                    users_collection.update_one({"_id": object_id}, {"$set": {"purchases": purchases}})
                    users_collection.update_one({"_id": object_id}, {"$set": {"categories": categories}})
                    return jsonify({"message": "Data added successfully"}), 200
                else:
                    return jsonify({"error": "User not found"}), 404
            else:
                return jsonify({"error": "User ID not provided"}), 400
        else:
            return jsonify({"error": "Data should be a list of dictionaries"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
