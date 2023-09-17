#Tribute
#  - to string
#  - from string

from abc import ABC, abstractmethod


class Tribute:

    def __init__(self, life, force, alliance, district):
        self.life = life
        self.force = force
        self.alliance = alliance
        self.district = district


    @staticmethod
    def from_string(tribute_str):
        if tribute_str == DeadTribute().__str__():
            return DeadTribute()
        elif tribute_str == LiveTribute().__str__():
            return LiveTribute()
        else:
            raise ValueError(f'Invalid tribute string: {tribute_str}')

    def __str__(self):
        raise NotImplementedError



class DeadTribute(Tribute):

    def __str__(self):
        if self.life == 0:
            return ' '

    def __eq__(self, other):
        return isinstance(other, DeadTribute)


class LiveTribute(Tribute):

    def __init__(self, actualPosition):
        self.actualPosition = actualPosition

    def __str__(self):
        if self.life != 0:
            res = 't' #+ self.district
            return res

    def __eq__(self, other):
        return isinstance(other, LiveTribute)