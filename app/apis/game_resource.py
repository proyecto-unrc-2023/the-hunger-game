from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from game.controllers.district_controller import DistrictController
from game.controllers.game_controller import GameController
from game.logic.game_logic import GameLogicSchema

games = {}

class ConfigDistrict(Resource):
    
    def get(self):
        d_controller = DistrictController()
        return d_controller.get_new_district()

    @jwt_required()
    def post(self):
        data = request.get_json()  #Obtain data sends by front.
        g_controller = GameController()
        new_game = g_controller.get_game(data) #Create a new game.
        
        if isinstance(new_game, str):
            return {"error": new_game}, 400
        
        game_id = get_jwt_identity() 
        games[game_id] = new_game
        return {'game_id': game_id}    

class Game(Resource):

    def put(self, game_id):
        game_id = int(game_id)
        if 0 < game_id:
            current_game = games[game_id]
            game_schema = GameLogicSchema()
            return {game_id: game_schema.dump(current_game)}
        else:
            return {'error': 'Game not found'}, 404
          
    def get(self, game_id):
        game_id = int(game_id)
        if 0 < game_id:
            current_game = games[game_id]
            controller = GameController() 
            next_iteration = controller.get_one_iteration(current_game)
            live_district = controller.pause_method(current_game)
            
            response = {game_id: next_iteration,
                        'pause': live_district}
            
            return response
        else:
            return {"error": "Game not found"}, 404
            
           