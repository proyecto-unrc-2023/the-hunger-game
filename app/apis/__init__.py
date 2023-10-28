from flask import Blueprint
from flask_restful import Api

from app.apis.game_resource import ConfigDistrict, AllDistrict, Game, NextIteration


# Create a blueprint
apis_bp = Blueprint('apis', __name__)
api = Api(apis_bp)

# Routes
api.add_resource(ConfigDistrict, '/district')
api.add_resource(AllDistrict, '/districts')
api.add_resource(Game, '/<string:game_id>')
api.add_resource(NextIteration, '/<string:game_id>/next_iteration')