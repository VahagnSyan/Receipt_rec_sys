"""
Module for processing images and extracting information.

This module provides functionality to process images, perform receipt recognition,
and extract information about products from the receipts.
"""

import os
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from recognition.recognition import receipt_recognition
from utils.utils import check_categories

load_dotenv()
client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]

process_images_bp = Blueprint("process_images", __name__)

UPLOAD_FOLDER = "./src/images"


@process_images_bp.route("/process-images", methods=["POST"])
def process_images():
    """
    Process uploaded images and extract information.

    This function handles POST requests to upload images, process them using receipt recognition,
    and extract information about products from the receipts. It then checks the categories
    of the extracted products against the user's preferences.

    Returns:
        JSON response indicating success or failure along with extracted product information.
    """

    if "images" not in request.files:
        return jsonify({"success": False, "message": "No image files provided"}), 400
    print(request.files)

    images = request.files.getlist("images")
    userID = request.form.get("id")
    results = []

    for image_file in images:
        if image_file.filename == "":
            return jsonify({"success": False, "message": "One or more selected files are empty"}), 400

        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_path)
        processed_text = receipt_recognition(image_path)
        check_categories(userID, processed_text)

        results.append({"filename": image_file.filename, "products": processed_text})

    return jsonify({"success": True, "results": results}), 200
