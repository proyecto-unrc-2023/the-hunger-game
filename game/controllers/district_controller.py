from flask import jsonify
from game.logic.district import DistrictSchema, District, DISTRICT_DEFAULT

class DistrictController:
    # Get initial stats own district.
    def get_new_district(self):
        district = dict(cant_tributes=4, life=50, force=5, alliance=3, cowardice=0)
        schema = DistrictSchema()
        result = jsonify(schema.dump(district))
        
        return result
    
    # Set the configuration own district.
    def set_district(self, cant_tributes, life, force, alliance, cowardice):
        District.set_config(self, life, force, alliance, DISTRICT_DEFAULT, cant_tributes, cowardice)
        return self
    