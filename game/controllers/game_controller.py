from flask import jsonify
from game.logic.game_logic import GameLogic, GameLogicSchema, GameMode
from game.logic.district import DISTRICT_DEFAULT

class GameController:
  
      def get_game(self, data):
        size = 20
        neutral_tributes = 10
        actual_game = GameLogic()
        actual_game.new_game(size, size)
        actual_game.set_parameters(DISTRICT_DEFAULT, data['life'], data['force'], data['alliance'], data['cant_tributes'], data['cowardice'])
        actual_game.configure_random_districts()
        actual_game.distribute_district_tributes()
        actual_game.distribute_neutral_tributes(neutral_tributes)
        actual_game.distribute_items()
        actual_game.mode = GameMode.SIMULATION
        return actual_game
  
      def get_one_iteration(self, actual_game: GameLogic):
        next_iteration = actual_game.one_iteration()

        if next_iteration is None:
            return {"error": "No data for next iteration"}

        schema = GameLogicSchema()
        result = schema.dump(next_iteration)
        return result
    