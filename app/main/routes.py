from flask import Blueprint
import secrets


main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def index():
    return "Hello! Welcome to the most secure comunication app in the world!"


@main_bp.route("/connect-to-server", methods=["POST"])
def connect_to_server():
    # Create a unique conversation_id for the client
    conversation_id = secrets.token_hex(32)
