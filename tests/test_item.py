import pytest

from game.logic.tribute import Tribute
from game.logic.item import Item, Poison, Potion, PotionForce, Weapon, WEAPON_EFFECT, POTION_EFFECT


def test_create_potion_from_str():
    res = Item.from_string('p ')
    assert res.__eq__(Potion())


def test_create_weapon_from_str():
    res = Item.from_string('w ')
    assert res.__eq__(Weapon())


def test_potion_apply_effect():
    tribute = Tribute()
    tribute.life = 75
    tribute.max_life = 100
    potion = Potion()
    potion.apply_effect(tribute)
    assert tribute.life.__eq__(75 + POTION_EFFECT)
    tribute1 = Tribute()
    tribute1.life = 100
    tribute1.max_life = 100
    potion1 = Potion()
    potion1.apply_effect(tribute1)
    assert tribute1.life.__eq__(100)

def test_potion_force_apply_effect():
    tribute = Tribute()
    potion = PotionForce()
    potion.apply_effect(tribute)
    assert tribute.force == 10
    tribute1 = Tribute()
    tribute1.force = 30
    potion1 = PotionForce()
    potion1.apply_effect(tribute1)
    assert tribute1.force == 30
    
def test_poison_apply_effect():
    tribute = Tribute()
    posion = Poison()
    posion.apply_effect(tribute)
    assert tribute.life == 45
    tribute1 = Tribute()
    tribute1.life = 5
    poison1 = Poison()
    poison1.apply_effect(tribute1)
    assert tribute1.life == 0
    with pytest.raises(ValueError):
        poison1.apply_effect(tribute1)
    

def test_weapon_apply_effect():
    tribute = Tribute()
    tribute.force = 6
    weapon = Weapon()
    weapon.apply_effect(tribute)
    assert tribute.force.__eq__(6 + WEAPON_EFFECT)


def test_potion_apply_effect_life_tribute_100_or_less_than_100():
    t1 = Tribute()
    t2 = Tribute()
    t3 = Tribute()
    t1.max_life = 100
    t2.max_life = 100
    t3.max_life = 100
    t1.life = 97
    t2.life = 99
    t3.life = 100
    potion = Potion()
    potion.apply_effect(t1)
    potion.apply_effect(t2)
    potion.apply_effect(t3)
    assert t1.life.__eq__(100)
    assert t2.life.__eq__(100)
    assert t3.life.__eq__(100)


def test_potion_get_pos():
    potion = Potion()
    potion.pos = (1, 1)

    res = potion.get_pos()
    assert res.__eq__((1, 1))


def test_weapon_get_pos():
    weapon = Weapon()
    weapon.pos = (3, 2)

    res = weapon.get_pos()
    assert res.__eq__((3, 2))


def test_potion_set_pos():
    potion = Potion()
    potion.set_pos((1, 2))

    res = potion.pos
    assert res.__eq__((1, 2))


def test_weapon_set_pos():
    weapon = Weapon()
    weapon.set_pos((2, 2))

    res = weapon.pos
    assert res.__eq__((2, 2))

# testing for create_item(..)

def test_create_item_potions_and_weapons():
    potion = Potion()
    number_potions = 8
    potion.create_item(number_potions)
    assert potion.cant_items == number_potions
    number_potions += 5
    potion.create_item(number_potions)
    assert potion.cant_items == 21

    weapon = Weapon()
    number_weapons = 10
    weapon.create_item(number_weapons)
    assert weapon.cant_items == number_weapons
    number_weapons += 8
    weapon.create_item(number_weapons)
    assert weapon.cant_items == 28


def test_create_invalid_input():
    potion = Potion()
    invalid_num_potion = -1
    with pytest.raises(ValueError):
        potion.create_item(invalid_num_potion)
    
    weapon = Weapon()
    invalid_num_weapon = -1
    with pytest.raises(ValueError):
        weapon.create_item(invalid_num_weapon)
