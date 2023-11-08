from flask import jsonify, request
from flask_restful import Resource
from app import db

from game.controllers.district_controller import DistrictController
from game.controllers.game_controller import GameController
from game.logic.game_logic import GameLogicSchema

games = []

class ConfigDistrict(Resource):
    
    def get(self):
        d_controller = DistrictController()
        return d_controller.get_new_district()
    
    def post(self):
        data = request.get_json()  # Obtengo los datos enviados por el cliente
        g_controller = GameController()
        first_game = g_controller.get_game(data) # Creo un juego con los datos obtenidos desde el front
        games.append(first_game)
        game_id = len(games) - 1
        return {'game_id': game_id}    

class Game(Resource):

    def put(self, game_id):
        game_id = int(game_id)
        if game_id < len(games):
            current_game = games[game_id]
            game_schema = GameLogicSchema()
            return {game_id: game_schema.dump(current_game)}
        else:
            return {'error': 'Game not found'}, 404

    def get(self, game_id):
        game_id = int(game_id)
        if game_id < len(games):
            current_game = games[game_id]
            controller = GameController() 
            next_iteration = controller.get_one_iteration(current_game)
            result_schema = GameLogicSchema()
            result = result_schema.dump(next_iteration)
            return {game_id: result}
        else:
            return {"error": "Game not found"}, 404