from marshmallow import Schema, fields

POTION_LIFE_EFFECT = 10

POTION_LIFE = 10
POTION_FORCE = 5
POTION_POISON = 5

WEAPON_EFFECT = 5

SWORD_EFFECT = 5
SPEAR_EFFECT = 3
RANGE_SPEAR = 1

BOW_EFFECT = 1
RANGE_BOW = 2


class Item:

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
        else:
            raise ValueError(f'Invalid object string: {object_str}')

    def __str__(self):
        pass

    def get_cant_items(self):
        return self.cant_items

    def get_pos(self):
        return self.pos

    def apply_effect(tribute):
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

    def create_potion(self, num_potion):
        pass


class PotionForce(Potion):

    # Potion force is pf.
    def __str__(self):
        return 'pf'

    def __eq__(self, other):
        return isinstance(other, PotionForce)

    # Apply effect of potion force to tribute. The force has no limit.
    def apply_effect(self, tribute):
        tribute.force += POTION_FORCE

    # Create potions force.
    def create_potion(self, num_potion):
        if num_potion < 0:
            raise ValueError(f'Invalid input number: {num_potion}')
        for i in range(num_potion):
            potion_force = PotionForce()
            self.items.append(potion_force)
            self.cant_items += 1


class PotionLife(Potion):

    # Potion life is pl.
    def __str__(self):
        return 'pl'

    def __eq__(self, other):
        return isinstance(other, PotionLife)

    # Apply effect of potion life to tribute.
    def apply_effect(self, tribute):
        if tribute.life == tribute.max_life or (tribute.life + POTION_LIFE > tribute.max_life):
            tribute.life = tribute.max_life
        if tribute.life + POTION_LIFE <= tribute.max_life:
            tribute.life += POTION_LIFE

    # Create potions life.
    def create_potion(self, num_potion):
        if num_potion < 0:
            raise ValueError(f'Invalid input number: {num_potion}')
        for i in range(num_potion):
            potion_life = PotionLife()
            self.items.append(potion_life)
            self.cant_items += 1


class PotionPoison(Potion):

    # Potion poison is po.
    def __str__(self):
        return 'po'

    def __eq__(self, other):
        return isinstance(other, PotionPoison)

    # Apply effect poison to tribute.
    def apply_effect(self, tribute):
        tribute.life -= POTION_POISON
        if tribute.is_dead():
            tribute.life = 0

    # Create potions poison.
    def create_potion(self, num_potion):
        if num_potion < 0:
            raise ValueError(f'Invalid input number: {num_potion}')
        for i in range(num_potion):
            potion_poison = PotionPoison()
            self.items.append(potion_poison)
            self.cant_items += 1


class Weapon(Item):

    def __str__(self):
        return 'w '

    def __eq__(self, other):
        return isinstance(other, Weapon)

    def apply_effect(self, tribute):
        if not tribute.weapon:
            tribute.force += WEAPON_EFFECT
            tribute.weapon = True
        else:
            raise ValueError("Tribute has a weapon already")

    def create_weapon(self, num_weapon):
        pass


class Sword(Weapon):

    # Sword is sw.
    def __str__(self):
        return 'sw'

    def __eq__(self, other):
        return isinstance(other, Sword)

    # Apply effect sword on tribute.
    def apply_effect(self, tribute):
        if not tribute.weapon:
            tribute.force += SWORD_EFFECT
            tribute.weapon = True
        else:
            raise ValueError("Tribute has a sword already")

    # Create weapons sword.
    def create_weapon(self, num_weapon):
        if num_weapon < 0:
            raise ValueError(f'Invalid input number: {num_weapon}')
        for i in range(num_weapon):
            sword = Sword()
            self.items.append(sword)
            self.cant_items += 1


class Spear(Weapon):

    # Spear is sp.
    def __str__(self):
        return 'sp'

    def __eq__(self, other):
        return isinstance(other, Spear)

    # Apply effect spear on tribute.
    def apply_effect(self, tribute):
        if not tribute.weapon:
            tribute.weapon = True
            tribute.range += RANGE_SPEAR
            tribute.force += SPEAR_EFFECT
        else:
            raise ValueError("Tribute has a spear already")

    # Create weapons spear.
    def create_weapon(self, num_weapon):
        if num_weapon < 0:
            raise ValueError(f'Invalid input number: {num_weapon}')
        for i in range(num_weapon):
            spear = Spear()
            self.items.append(spear)
            self.cant_items += 1


class Bow(Weapon):

    # Bow is wo.
    def __str__(self):
        return 'wo'

    def __eq__(self, other):
        return isinstance(other, Bow)

    # Apply effect bow on tribute.
    def apply_effect(self, tribute):
        if not tribute.weapon:
            tribute.force += BOW_EFFECT
            tribute.weapon = True
            tribute.range += RANGE_BOW
        else:
            raise ValueError("Tribute has a bow already")

    # Create weapons bow.
    def create_weapon(self, num_weapon):
        if num_weapon < 0:
            raise ValueError(f'Invalid input number: {num_weapon}')
        for i in range(num_weapon):
            bow = Bow()
            self.items.append(bow)
            self.cant_items += 1


class ItemSchema(Schema):
    name = fields.Function(lambda obj: obj.__str__())
    mode = fields.Str()
    effect = fields.Integer()
    # name = fields.Function(self.__str__())
