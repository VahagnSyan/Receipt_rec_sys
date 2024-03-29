from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from recognition.recognition import receipt_recognition
from utils.utils import check_categories
from flask_cors import CORS


load_dotenv()

client = MongoClient(os.environ.get("MONGO_URI"))
db = client[os.environ.get("DB_NAME")]
users_collection = db["users"]

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "./src/images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/process-images", methods=["POST"])
def process_images():
    if "images" not in request.files:
        return jsonify({"success": False, "message": "No image files provided"}), 400

    images = request.files.getlist("images")
    userID = request.form.get("id")
    
    results = []
    
    for image_file in images:
        if image_file.filename == "":
            return jsonify({"success": False, "message": "One or more selected files are empty"}), 400
        
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
        image_file.save(image_path)
        processed_text = receipt_recognition(image_path)
        check_categories(userID, processed_text)
        
        results.append({"filename": image_file.filename, "products": processed_text})
    
    return jsonify({"success": True, "results": results}), 200

if __name__ == "__main__":
    app.run(debug=True)
