import json

from flask import request, Response
from werkzeug.exceptions import abort

from discount import create_app_for_triggered_event


def get_app_context():
    app = create_app_for_triggered_event()
    app.app_context().push()


def get_json_or_abort() -> dict:
    json_data: dict = request.json
    if not json_data:
        abort(Response(json.dumps({'message': "No input data provided"}), status=400))

    return json_data
