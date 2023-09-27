#Object
#  - to string
#  - from string

from abc import ABC, abstractmethod

class Item:

    def __init__(self, name):
        self.name == name
        self.value == None

    
    @staticmethod
    def from_string(object_str):
        if object_str == Potion().__str__():
            return Potion()
        elif object_str == Weapon().__str__():
            return Weapon()
        else:
            raise ValueError(f'Invalid object string: {object_str}')

    def __str__(self):
        raise NotImplementedError



class Potion(object):

    def __str__(self):
        return 'p'

    def __eq__(self, other):
        return isinstance(other, Potion)


class Weapon(object):

    def __str__(self):
        return 'w'

    def __eq__(self, other):
        return isinstance(other, Weapon)