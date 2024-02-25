from flask import Blueprint

communicator_bp = Blueprint("communicator_bp", __name__)

from app.communicator import routes
