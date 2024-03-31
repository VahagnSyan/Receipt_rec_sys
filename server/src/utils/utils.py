"""
User Purchases Processing Module.

This module provides functionality to preprocess user purchases data
and check categories for processed text against user preferences.
"""


import os
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]


def preprocess_purchases(purchases):
    """
    Preprocesses the purchases data into a dictionary for faster lookup.

    Args:
        purchases (list): List of purchase dictionaries.

    Returns:
        dict: Dictionary with purchase names as keys and categories as values.
    """
    purchases_dict = {}
    for purchase in purchases:
        purchases_dict[purchase['name']] = purchase['category']
    return purchases_dict


def check_categories(user_id, processed_text):
    """
    Check categories for processed text against user preferences.

    Args:
        user_id (str): The user ID.
        processed_text (list): List of dictionaries containing processed text data.

    Returns:
        None
    """
    object_id = ObjectId(user_id)
    user_data = users_collection.find_one({"_id": object_id})
    purchases = user_data.get("purchases", [])
    purchases_dict = preprocess_purchases(purchases)
    for item in processed_text:
        name = item.get('name')
        category = purchases_dict.get(name)
        if category:
            item['category'] = category
