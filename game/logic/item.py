# Object
#  - to string
#  - from string


class Item:

    def __init__(self):
        self.pos = None

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

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def apply_effect(tribute):
        raise NotImplementedError


class Potion(Item):

    def __str__(self):
        return 'p'

    def __eq__(self, other):
        return isinstance(other, Potion)

    def apply_effect(self, tribute):
        if tribute.life < 100:
            tribute.life += 5
            if tribute.life > 100:
                tribute.life = 100 


class Weapon(Item):

    def __str__(self):
        return 'w'

    def __eq__(self, other):
        return isinstance(other, Weapon)

    def apply_effect(self, tribute):
        tribute.force += 1
