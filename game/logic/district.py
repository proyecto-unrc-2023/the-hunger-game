import random

from game.logic.tribute import Tribute
from marshmallow import Schema, fields

TRIBUTES_DEFAULT = 4
DISTRICT_DEFAULT = 0

class District:

    # Constructor of District class where initializes all attributes
    def __init__(self):
        self.number_district = None
        self.cant_tributes = 0
        self.tributes = []
        self.chars = ['t','a','b','c','d','e','f','g','h','i','j','k','l','m']


    # Return number_district attribute
    def get_number_district(self):
        return self.number_district

    # Return cant_tribute attribute
    def get_cant_tribute(self):
        return self.cant_tributes

    # Configure own tributes with life, force, alliance, number of district and
    # numbers of tributes.
    def set_config(self, life, force, alliance, number_district, cant_tributes, cowardice):
        self.number_district = number_district
        self.cant_tributes = cant_tributes
        for i in range(cant_tributes):
            tribute = Tribute()
            self.asign_name_tribute(tribute)
            tribute.set_config_parameters(life, force, alliance, number_district, cowardice)
            self.tributes.append(tribute)

    # Create a district of tributes with random force and alliance, were these stats never are high.
    def set_config_random(self, num_district):
        self.cant_tributes = TRIBUTES_DEFAULT
        self.number_district = num_district
        for t in range(self.cant_tributes):
            tribute = Tribute()
            self.asign_name_tribute(tribute)
            while True:
                tribute.force = random.randint(5, 10)
                tribute.alliance = random.randint(3, 10)
                if tribute.force + tribute.alliance <= 15:
                    break
            tribute.district = num_district
            self.tributes.append(tribute)

    # Add one tribute in a list of tributes.
    def add_tribute(self, tribute):
        if not isinstance(tribute, Tribute):
            raise ValueError(f'Is not an instance of Tribute: {tribute}')

        self.tributes.append(tribute)
        self.cant_tributes += 1

    # Remove one tribute in a list
    def remove_tribute(self, tribute):
        for tr in self.tributes:
            if tribute.__eq__(tr):
                self.tributes.remove(tr)
                self.cant_tributes -= 1

    # Method to assign a name for the tributes of the district
    def asign_name_tribute(self, tribute):
        tribute.name = self.chars.pop(0) + str(self.number_district)
        

class DistrictSchema(Schema):
    from game.logic.tribute import TributeSchema
    
    number_district = fields.Integer()
    cant_tributes = fields.Integer()
    tributes = fields.Nested(TributeSchema(), many=True)
    life = fields.Integer()
    force = fields.Integer()
    alliance = fields.Integer()
    cowardice = fields.Integer()
