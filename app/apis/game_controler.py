from flask_restful import Resource
from flask import Blueprint
from game.logic.district import District, DistrictSchema
from flask_restful import Api
from flask import jsonify

game_bp = Blueprint('game', __name__)
game_api = Api(game_bp)

class GameControler(Resource):
    def get_new_district(self):
        t1 = dict(name='David Bowie', life=50, force=5, alliance=1,cowardice=0,district=4,pos=(0,0))
        t2 = dict(name='David Bowie', life=50, force=5, alliance=1,cowardice=0,district=4,pos=(0,1))
        district = dict(number_district=4, cant_tributes=1, tributes=(t1,t2), life=50, force=5, alliance=1, cowardice=0)
        schema = DistrictSchema()
        result = jsonify(schema.dump(district))
        
        return result
    
    def get(self):
        game = GameControler()
        return game.get_new_district()

game_api.add_resource(GameControler, '/district')
