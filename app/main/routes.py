from flask import Blueprint, jsonify
import secrets


main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def index():
    return "Hello! Welcome to the most secure comunication app in the world!"


# This route will be used to connect to the server to see if the server is up
@main_bp.route("/connect-to-server", methods=["POST"])
def connect_to_server():
    return jsonify({"status": "success", "message": "The server is up and running!"})