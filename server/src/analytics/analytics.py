from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from recognition.recognition import receipt_recognition
from utils.utils import check_categories
from bson import ObjectId
from datetime import datetime

load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]

analytics_bp = Blueprint("analytics", __name__)

UPLOAD_FOLDER = "./src/images"


def difference(date1, date2):
    date_format = "%d/%m/%Y"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    difference = datetime1 - datetime2
    return difference.days >= 0


@analytics_bp.route("/analytics", methods=["POST"])
def analytics():
    user_id = request.json.get("id")
    if not user_id:
        return jsonify({"error": "User ID not provided"}), 400
    object_id = ObjectId(user_id)
    user = users_collection.find_one({"_id": object_id})
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    current_date = datetime.now()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    date = f'{day}/{month}/{year}'
    purchases = user.get("purchases", [])

    result = []
    for element in purchases:
        if difference(date, element.get('date')):
            result.append(element)
    
    return jsonify({"purchases": result}), 200
