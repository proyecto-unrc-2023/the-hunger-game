from game.logic.tribute import MAX_FORCE

POTION_LIFE_EFFECT = 10
POTION_FORCE_EFFECT = 5
WEAPON_EFFECT = 5
POISON_EFFECT = 5

class Item():

    def __init__(self):
        self.pos = None
        self.cant_items = 0
        self.items = []

    @staticmethod
    def from_string(object_str):
        if object_str == Potion().__str__():
            return Potion()
        elif object_str == Weapon().__str__():
            return Weapon()
        elif object_str == Poison().__str__():
            return Poison()
        else:
            raise ValueError(f'Invalid object string: {object_str}')

    def __str__(self):
        pass

    def get_pos(self):
        return self.pos
    
    def get_cant_items(self):
        return self.cant_items
    
    def apply_effect(tribute):
        pass

    def create_item(number_item):
        pass

    def is_weapon(self):
        return isinstance(self, Weapon)

    def is_potion(self):
        return isinstance(self, Potion)

class Potion(Item):

    def __str__(self):
        return 'p '

    def __eq__(self, other):
        return isinstance(other, Potion)

    def apply_effect(self, tribute):
        if tribute.life == tribute.max_life:
            tribute.life += 0
        if tribute.life + POTION_LIFE_EFFECT > tribute.max_life:
            effect = tribute.max_life - tribute.life
            tribute.life += effect
        if tribute.life + POTION_LIFE_EFFECT < tribute.max_life:
            tribute.life += POTION_LIFE_EFFECT

    # Add an item potion in a list of items.
    def create_item(self, number_item):
        if number_item < 0:
            raise ValueError(f'Invalid input number: {number_item}')
        for i in range(number_item):
            potion = Potion()
            self.items.append(potion)
            self.cant_items += 1 

class PotionForce(Item):

    def __str__(self):
        return 'pf'

    def __eq__(self, other):
        return isinstance(other, PotionForce)

    def apply_effect(self, tribute):
        if tribute.force == MAX_FORCE:
            tribute.force += 0
        if tribute.force + POTION_FORCE_EFFECT > MAX_FORCE:
            tribute.force = MAX_FORCE
        if tribute.force + POTION_FORCE_EFFECT < MAX_FORCE:
            tribute.force += POTION_FORCE_EFFECT

class Poison(Item):

    def __str__(self):
        return 'po'

    def __eq__(self, other):
        return isinstance(other, Poison)

    def apply_effect(self, tribute):
        if tribute.is_dead():
            raise ValueError("Dead tribute trying take a poison.")
        tribute.life -= POISON_EFFECT


class Weapon(Item):

    def __str__(self):
        return 'w '

    def __eq__(self, other):
        return isinstance(other, Weapon)

    def apply_effect(self, tribute):
        if not tribute.weapon:
            tribute.force += WEAPON_EFFECT
            tribute.weapon = True
        #else:
        #    raise ValueError("Tribute has a weapon already")

    # Add an item weapon in a list of items. 
    def create_item(self, number_item):
        if number_item < 0:
            raise ValueError(f'Invalid input number: {number_item}')
        for i in range(number_item):
            weapon = Weapon()
            self.items.append(weapon)
            self.cant_items += 1