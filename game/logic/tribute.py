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
        if tribute_str == Tribute().__str__():
            return 't'
        else:
            raise ValueError(f'Invalid tribute string: {tribute_str}')

    def __str__(self):
        return 't'