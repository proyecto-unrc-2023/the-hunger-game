from flask import jsonify, request
from flask_restful import Api, Resource
from pytest import console_main

from game.controllers.district_controller import DistrictController
from game.logic.game_logic import GameLogic, GameLogicSchema, GameMode

games = {}
class ConfigDistrict(Resource):
    
    def get(self):
        d_controller = DistrictController()
        return d_controller.get_new_district()
    
    def post(self):
        data = request.get_json()  # Obtengo los datos enviados por el cliente
        print(data) # Imprimo los datos por consola
        return jsonify({'message': 'Datos recibidos correctamente'})    

class AllDistrict(Resource):

    def get(self):
        controller = DistrictController()
        return controller.get_districts()

    
    def post(self):
        data = request.get_json()
        print(data)
        return jsonify({'message': 'Datos recibidos correctamente'})

class Game(Resource):

    def put(self, game_id):
        size = 20
        num_district = 0
        cant_neutral_tributes = 10
        life, force, alliance, cant_tributes, cowardice = 55, 7, 1, 6, 1
        actual_game = GameLogic()
        games[game_id] = actual_game
        game_schema = GameLogicSchema()
        actual_game.new_game(size, size)
        actual_game.configure_random_districts()
        actual_game.set_parameters(num_district, life, force, alliance, cant_tributes, cowardice)
        actual_game.distribute_tributes()
        actual_game.distribute_items()
        actual_game.distribute_neutral_tributes(cant_neutral_tributes)
        actual_game.mode = GameMode.SIMULATION
        return {game_id: game_schema.dump(actual_game)}

    def get(self, game_id):
        if game_id not in games:
            return {"error": "Game not found"}, 404

        game = games[game_id]
        game_schema = GameLogicSchema()
        return {game_id: game_schema.dump(game)}

class NextIteration(Resource):

    def get(self, game_id):
        if game_id not in games:
            return {"error": "Game not found"}, 404
        actual_game = games[str(game_id)]
        controller = DistrictController()
        next_iteration = controller.get_one_iteration(actual_game)
        result_schema = GameLogicSchema()
        result = result_schema.dump(next_iteration)
        return {game_id: result}
    