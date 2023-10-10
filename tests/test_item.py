import pytest

from game.logic.tribute import Tribute
from game.logic.item import Item, Potion, Weapon, WEAPON_EFFECT, POTION_EFFECT


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
