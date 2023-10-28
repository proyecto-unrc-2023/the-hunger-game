from flask import Blueprint
from flask_restful import Api

from app.apis.game_resource import ConfigDistrict, Game


# Create a blueprint
apis_bp = Blueprint('apis', __name__)
api = Api(apis_bp)

# Routes
api.add_resource(ConfigDistrict, '/district')
api.add_resource(Game, '/<string:game_id>')