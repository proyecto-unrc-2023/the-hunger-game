

from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from app.apis.db import Game

from game.logic.game_logic import GameLogicSchema

game_bp = Blueprint('game', __name__)
game_api = Api(game_bp)


class GameResource(Resource):
    from app.apis.db import Game

    
    def get(self, game_id):
        game_schema  = GameLogicSchema() 

        game = Game.query.filter(id=game_id).first() 

        return jsonify(game_schema.dump(game)) 
    
game_api.add_resource(GameResource, '/gamelogic') 
