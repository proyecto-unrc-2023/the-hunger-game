

from flask import jsonify, request
from flask_restful import Api, Resource
from game.controllers.district_controller import DistrictController

from game.logic.game_logic import GameLogic, GameLogicSchema

games = {}

class Game(Resource):

    def put(self,game_id):
        actual_game = GameLogic()
        games[game_id] = request.form[actual_game] 
        return {game_id: games[game_id]}    

    def get(self, game_id):
        game_schema  = GameLogicSchema() 
         
        
        game = games[game_id] 

        return jsonify(game_schema.dump(game)) 


class ConfigDistrict(Resource):
    
    def get(self):
        d_controller = DistrictController()
        return d_controller.get_new_district()
    
    def post(self):
        return 0        

    

