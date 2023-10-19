from flask import Blueprint, jsonify


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/api/some_endpoint', methods=['GET'])
def get_data():
    return jsonify({"data": "Datos de ejemplo"})
