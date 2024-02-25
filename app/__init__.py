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

    # Get the secret key from the configuration file
    app.secret_key = app.config["SECRET_KEY"]

    # Load the environment variables
    load_dotenv()

    # Load the appropriate config file
    if os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("instance.config.DevelopmentConfig")
    elif os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object("instance.config.TestingConfig")
    elif os.environ.get("FLASK_ENV") == "production":
        app.config.from_object("instance.config.ProductionConfig")
    else:
        print("FLASK_ENV environment variable is not set!")

    # Register blueprints withinn app context
    from app.main import main_bp
    from app.communicator import communicator_bp

    # Register the blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(communicator_bp)

    return app
