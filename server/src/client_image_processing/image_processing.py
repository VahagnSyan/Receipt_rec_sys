from flask import Flask, request, jsonify
from pymongo import MongoClient
from hashlib import sha256
from dotenv import load_dotenv
import os
from PIL import Image
import pytesseract
from preprocessing.preprocessing import Preprocessing
from preprocessing.post_processing import Post_Processing
from preprocessing.detection import Detection

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

    # Save the uploaded image to the 'uploads' folder
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
    image_file.save(image_path)

    # Perform image preprocessing (You can replace this with your actual preprocessing code)
    processed_text = preprocess_image(image_path)
    
    # Return the processed text to the client
    return jsonify({"success": True, "processed_text": processed_text}), 200


def preprocess_image(image_path):
    # Example: Use pytesseract to extract text from the image
    # img = Image.open(image_path)
    # text = pytesseract.image_to_string(img)
    # return text

    preprocess = Preprocessing(image_path)
    text = preprocess.process_image()
    post = Post_Processing(text)
    post_text = post.post_process()
    data = Detection(post_text)
    return data.detection()


if __name__ == "__main__":
    app.run(debug=True)
