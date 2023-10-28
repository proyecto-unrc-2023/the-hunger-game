from flask import jsonify
from game.logic.district import DistrictSchema, District
from game.logic.game_logic import GameLogic, GameLogicSchema


class DistrictController:
    
    def get_new_district(self):
        district = dict(cant_tributes=4, life=50, force=5, alliance=1, cowardice=0)
        schema = DistrictSchema()
        result = jsonify(schema.dump(district))
        
        return result
    
    def set_district(self, cant_tributes, life, force, alliance, cowardice):
        District.set_config(self, life, force, alliance, 0, cant_tributes, cowardice)
        return self
    
    # Get own district and random district
    def get_districts(self):
        own_district = self.get_new_district() #almaceno el json envuelto en HTTP del distrito propio
        game = GameLogic()
        game.configure_random_districts() #configuro 5 distritos aleatorios
        
        serialize_list = []
        for district in game.districts:
            schema = DistrictSchema()
            serialize_district = schema.dump(district)
            serialize_list.append(serialize_district)

        
        # diccionario donde almacenos los json
        response_dict = {
            "Distrito propio": own_district.get_json(),
            "Distritos enemigos": serialize_list
        }

        return jsonify(response_dict)
    

    def get_one_iteration(self, actual_game: GameLogic):
        next_iteration = actual_game.one_iteration()

        if next_iteration is None:
            return {"error": "No data for next iteration"}

        schema = GameLogicSchema()
        result = schema.dump(next_iteration)
        return result
    
