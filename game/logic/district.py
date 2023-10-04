from game.logic.tribute import Tribute
import random


class District:

    # Constructor of District class where initializes all atributes
    def __init__(self):
        self.number_district = None
        self.cant_tributes = 0
        self.tributes = []

    # Return number_district atribute
    def get_number_district(self):
        return self.number_district

    # Return cant_tribute atribute
    def get_cant_tribute(self):
        return self.cant_tributes

    # Configure own tributes with life, force, alliance, number of district and
    # numbers of tributes.
    def set_config(self, life, force, alliance, number_district, cant_tributes):

        if life < 0:
            raise ValueError(f'Life can not be negative: {life}')
        if force < 5 or force > 10:
            raise ValueError(f'Force must be between 5 and 10 points: {force}')
        if alliance < 1 or alliance > 10:
            raise ValueError(f'Alliance must be between 1 and 10 points: {alliance}')
        if number_district < 1:
            raise ValueError(f'Number of district can not be less than 1: {number_district}')

        self.number_district = number_district  # setea el numero del distrito
        self.cant_tributes = cant_tributes  # setea la cantidad de tributos en el distrito

        for i in range(self.cant_tributes):
            trib = Tribute()
            trib.life = life  # setea la vida
            trib.force = force  # setea la fuerza
            trib.alliance = alliance  # setea la alianza
            trib.district = number_district  # setea el numero del distrito
            self.tributes.append(trib)  # se agrega el tributo configurado

    # Configure tributes of an district with random stats.
    def set_config_random(self, num_district):
        for i in range(4):
            trib = Tribute()
            trib.life = 50
            trib.force = random.randint(5, 10)
            trib.alliance = random.randint(1, 10)
            trib.district = num_district
            self.tributes.append(trib)  # se agrega el tributo configurado

    # Add one tribute in a list of tributes.
    def add_tribute(self, tribute):
        if not isinstance(tribute, Tribute):
            raise ValueError(f'Is not an instance of Tribute: {tribute}')

        self.tributes.append(tribute)
        self.cant_tributes = self.cant_tributes + 1

    def remove_tribute(self, tribute):
        if not (tribute in self.tributes):
            raise ValueError(f'tribute is not of this district')
        self.tributes.remove(tribute)
        self.cant_tributes = self.cant_tributes - 1
