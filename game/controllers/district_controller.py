from flask import jsonify
from game.logic.district import DistrictSchema, District


class DistrictController:
    def get_new_district(self):
        district = dict(cant_tributes=6,life=50, force=5, alliance=1, cowardice=0)
        schema = DistrictSchema()
        result = jsonify(schema.dump(district))
        
        return result
    
    def get_district_init(self, cant_tributes, life, force, alliance, cowardice):
        District.set_config(self,life,force,alliance,0,cant_tributes,cowardice)

        return self
    