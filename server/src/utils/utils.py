from flask import Flask, request, jsonify
from bson import ObjectId
from pymongo import MongoClient
from hashlib import sha256
from dotenv import load_dotenv
import os


load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]


def check_categories(userID, processed_text):
    object_id = ObjectId(userID)
    user_data = users_collection.find_one({"_id": object_id})
    categories = user_data.get("categories", [])
    purchases = user_data.get("purchases", [])
    for item in processed_text:
        print(item.get('name'))