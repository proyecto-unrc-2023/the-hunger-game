#Object
#  - to string
#  - from string

from abc import ABC, abstractmethod

class Object:

    def __init__(self, name):
        self.name = name
        self.place = None
        self.used = None

    @staticmethod
    def from_string(object_str):
        if object_str == Potion().__str__(False) or object_str == Potion().__str__(True):
            return Potion()
        elif object_str == Weapon().__str__(False) or object_str == Weapon().__str__(True):
            return Weapon()
        else:
            raise ValueError(f'Invalid object string: {object_str}')

    def __str__(self):
        raise NotImplementedError

    def applies_efects(tribute):
        raise NotImplementedError

class Potion(object):

    def __str__(self, used):
        if used == False:
            return 'p'
        else:
            return '-p'

    def __eq__(self, other):
        return isinstance(other, Potion)
      
    def applies_efects(tribute):
      tribute.life += 5
      
      
class Weapon(object):

    def __str__(self, used):
        if used == False:
            return 'w'
        else:
            return '-w'

    def __eq__(self, other):
        return isinstance(other, Weapon)
      
    def applies_efects(tribute):
      tribute.force += 1