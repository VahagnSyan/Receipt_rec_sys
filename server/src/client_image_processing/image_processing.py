from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from recognition.recognition import receipt_recognition
from utils.utils import check_categories


load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]

app = Flask(__name__)

UPLOAD_FOLDER = "./src/images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/process-image", methods=["POST"])
def process_image():
    if "image" not in request.files:
        return jsonify({"success": False, "message": "No image file provided"}), 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return jsonify({"success": False, "message": "No selected file"}), 400

    image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
    image_file.save(image_path)
    processed_text = receipt_recognition(image_path)
    check_categories('65f094c80c8e3a2d123845ee', processed_text)
    return jsonify({"success": True, "processed_text": processed_text}), 200


if __name__ == "__main__":
    app.run(debug=True)
