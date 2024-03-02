from flask import Blueprint, request, jsonify
from . import communicator_bp


@communicator_bp.route("/communicator", methods=["POST"])
def communicator():
    data = request.get_json()
    return jsonify(data)
