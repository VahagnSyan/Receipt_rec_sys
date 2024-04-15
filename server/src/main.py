from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from authentication.authentication import auth_bp
from client_image_processing.image_processing import process_images_bp
from client_image_processing.add_purchases import add_bp
from analytics.analytics import analytics_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(add_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(process_images_bp)
app.register_blueprint(analytics_bp)

if __name__ == "__main__":
    app.run(debug=True)
