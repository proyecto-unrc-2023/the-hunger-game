import random

from game.logic.tribute import Tribute

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
        self.number_district = number_district
        self.cant_tributes = cant_tributes
        
        letters = 'tabcdefghijklm'
        for i in range(cant_tributes):
            tribute = Tribute()
            tribute.name = letters[i+1] + str(number_district)
            tribute.set_config_parameters(life, force, alliance, number_district)
            tribute.configured = True
            self.tributes.append(tribute)

    # Configure tributes of an district with random stats.
    def set_config_random(self, num_district):
        self.number_district = num_district
        for i in range(4):
            tribute = Tribute()
            tribute.life = 50
            tribute.force = random.randint(5, 10)
            tribute.alliance = random.randint(3, 10)
            tribute.district = num_district
            self.tributes.append(tribute)

    # Create own district with minimal values.  
    def set_config_by_default(self, num_district):
        self.cant_tributes = 4
        self.number_district = num_district
        letters = 'tabcdefghijklm'
        for t in range(self.cant_tributes):
            tribute = Tribute()
            tribute.name = letters[t] + str(num_district)
            tribute.life = 50
            tribute.force = 5
            tribute.alliance = 3
            tribute.district = num_district
            self.tributes.append(tribute)

    # Add one tribute in a list of tributes.
    def add_tribute(self, tribute):
        if not isinstance(tribute, Tribute):
            raise ValueError(f'Is not an instance of Tribute: {tribute}')

        self.tributes.append(tribute)
        self.cant_tributes = self.cant_tributes + 1

    # Remove one tribute in a list
    def remove_tribute(self, tribute):
        for tr in self.tributes:
            if tribute.name == tr.name:
                self.tributes.remove(tr)
                self.cant_tributes = self.cant_tributes - 1

    # Add one more tribute in own district, if points not are less than four. So can buy a new tribute 
    def buy_tribute(self, points):
        if points < 4:
            raise ValueError(f'The points that you have not enough for buy one tribute: {points}')
        
        tribute = Tribute()
        price_tribute = 4
        points -= price_tribute 
        self.tributes.append(tribute)
        self.cant_tributes += 1

        return points