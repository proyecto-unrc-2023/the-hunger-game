import random

from game.logic.tribute import Tribute, TributeSchema
from marshmallow import Schema, fields

TRIBUTES_DEFAULT = 4


class District:

    # Constructor of District class where initializes all attributes
    def __init__(self):
        self.number_district = None
        self.cant_tributes = 0
        self.tributes = []

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
        letters = 'tabcdefghijklm'
        for i in range(cant_tributes):
            tribute = Tribute()
            tribute.name = letters[i + 1] + str(number_district)
            tribute.set_config_parameters(life, force, alliance, number_district)
            tribute.cowardice = cowardice
            tribute.configured = True
            self.tributes.append(tribute)

    # Create a district of tributes with random force and alliance, were these stats never are high.
    def set_config_by_default(self, num_district):
        self.cant_tributes = TRIBUTES_DEFAULT
        self.number_district = num_district
        letters = 'tabcdefghijklm'
        for t in range(self.cant_tributes):
            tribute = Tribute()
            tribute.name = letters[t] + str(num_district)
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
            if tribute.name == tr.name:
                self.tributes.remove(tr)
                self.cant_tributes -= 1


class DistrictSchema(Schema):
    number_district = fields.Integer()
    cant_tributes = fields.Integer()
    tributes = fields.Nested(TributeSchema, many=True)
