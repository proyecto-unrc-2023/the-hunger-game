from flask_restful import Resource
from flask import Blueprint
from flask_restful import Api
from game.controllers.district_controller import DistrictController

config_bp = Blueprint('game', __name__)
district_api = Api(config_bp)


class ConfigBp(Resource):
    
    def get(self):
        d_controller = DistrictController()
        return d_controller.get_new_district()
    
    def post(self):
        return 0        
    
district_api.add_resource(ConfigBp, '/district')


