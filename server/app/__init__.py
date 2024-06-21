from flask import Flask
from flask_cors import CORS
from app.api.video_routes import video_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(video_bp)
    return app
