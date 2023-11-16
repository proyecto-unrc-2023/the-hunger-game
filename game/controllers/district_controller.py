from flask import jsonify
from game.logic.district import DistrictSchema, TRIBUTES_DEFAULT
from game.logic.tribute import LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT, COWARDICE_DEFAULT

class DistrictController:
    # Get initial stats own district.
    def get_new_district(self):
        district = dict(cant_tributes=TRIBUTES_DEFAULT, 
                        life=LIFE_DEFAULT, 
                        force=FORCE_DEFAULT, 
                        alliance=ALLIANCE_DEFAULT, 
                        cowardice=COWARDICE_DEFAULT)
        schema = DistrictSchema()
        result = jsonify(schema.dump(district))
        
        return result
    