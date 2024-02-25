from flask import Blueprint, jsonify
import secrets


main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def index():
    return "Hello! Welcome to the most secure comunication app in the world!"
