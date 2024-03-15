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


def preprocess_purchases(purchases):
    """
    Preprocesses the purchases data into a dictionary for faster lookup.
    """
    purchases_dict = {}
    for purchase in purchases:
        purchases_dict[purchase['name']] = purchase['category']
    return purchases_dict


def check_categories(userID, processed_text):
    object_id = ObjectId(userID)
    user_data = users_collection.find_one({"_id": object_id})
    purchases = user_data.get("purchases", [])
    
    purchases_dict = preprocess_purchases(purchases)
    
    for item in processed_text:
        name = item.get('name')
        category = purchases_dict.get(name)
        if category:
            item['category'] = category