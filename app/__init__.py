from flask import Flask
from dotenv import load_dotenv
import os


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    