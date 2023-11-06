from flask import jsonify
from game.logic.game_logic import GameLogic, GameLogicSchema, GameMode
from game.logic.district import DISTRICT_DEFAULT

class GameController:
      # Set up a game.  
      def get_game(self, data):
        game = GameLogic()
        game.new_game(15, 15)
        game.set_parameters(DISTRICT_DEFAULT, data['life'], data['force'], data['alliance'], data['cant_tributes'], data['cowardice'])
        game.configure_random_districts()
        game.distribute_district_tributes()
        game.distribute_neutral_tributes(10)
        game.distribute_items()
        game.mode = GameMode.SIMULATION
        return game

      # This method takes the current state of game, do an iteration, and
      # return the update state serialized in readable format. 
      def get_one_iteration(self, game: GameLogic):
        next_iteration = game.one_iteration_front()
        if next_iteration is None:
            return {"error": "No data for next iteration"}
        next_iteration.winner_district()
        schema = GameLogicSchema()
        
        result = schema.dump(next_iteration)
        
        return result
    
     # Returns the number of the winner district.
      def get_winner_district(self, actual_game):
          winner = actual_game.winner_district()
          schema = GameLogicSchema()
          
          result = schema.dump(winner) 
           
          return result
      
      def pause_method(self):
          lives = self.tributes_lives()
          schema = GameLogicSchema()
          result = schema.dump(lives)

          return result