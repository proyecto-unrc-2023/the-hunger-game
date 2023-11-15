from flask import Blueprint
from flask_restful import Api

from app.apis.user_resource import Structure, Register, SelectPj, UserGet, Login, UserIdGet
from app.apis.game_resource import ConfigDistrict, Game

# Create a blueprint
apis_bp = Blueprint('apis', __name__)
api = Api(apis_bp)

# Routes
api.add_resource(ConfigDistrict, '/district')
api.add_resource(Game, '/<int:game_id>')
api.add_resource(Structure, '/db')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(UserGet, '/get_user')
api.add_resource(SelectPj, '/select')
api.add_resource(UserIdGet, '/get_id')

