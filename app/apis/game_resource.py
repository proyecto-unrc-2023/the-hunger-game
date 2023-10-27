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