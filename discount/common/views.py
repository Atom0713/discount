from flask import Blueprint, jsonify

bp = Blueprint("common", __name__)


@bp.route("/")
def index():
    return jsonify({'status': 'ok', 'message': 'Server is running.'})
