#Tribute
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
        return ' '

    def __eq__(self, other):
        return isinstance(other, DeadTribute)


class LiveTribute(Tribute):

    def __init__(self):
        self.pos = None

    def __str__(self):
        return 't'


    def __eq__(self, other):
        return isinstance(other, LiveTribute)