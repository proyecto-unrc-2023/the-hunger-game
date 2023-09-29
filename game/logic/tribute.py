# Tribute
#  - to string
#  - from string

from abc import ABC, abstractmethod


class Tribute:

    def __init__(self):
        self.life = None
        self.force = None
        self.alliance = None
        self.district = None
        self.pos = None

    @staticmethod
    def from_string(tribute_str):
        if tribute_str == Tribute().__str__():
            return 't'
        else:
            raise ValueError(f'Invalid tribute string: {tribute_str}')

    def is_alive(self):
        if self.life > 0:
            return True

    def is_dead(self):
        if self.life == 0:
            return True

    def __str__(self):
        return 't'
    
    def atack_to(self, tribute, board):
        listadj = board.get_adjacent_positions(self.pos[0], self.pos[1])
        if (tribute.pos[0], tribute.pos[1]) in listadj:
            tribute.life -= self.force
        else:
            raise ValueError(f"Not possible attack")

        if (self.district == None):
            return 't'
        else:
            # return 't' + str(self.district)
            return 't' + str(self.district.get_number_district())

    def set_cofing(self, life, force, alliance, district):
        self.life = life
        self.force = force
        self.alliance = alliance
        self.district = district
