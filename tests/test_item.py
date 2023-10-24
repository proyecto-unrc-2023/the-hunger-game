import pytest

from game.logic.tribute import Tribute, LIFE_DEFAULT, FORCE_DEFAULT
from game.logic.item import Potion, PotionForce, PotionLife, PotionPoison, Weapon, \
                            Sword, Spear, Bow
from game.logic.item import POTION_FORCE, POTION_LIFE, POTION_POISON, SWORD_EFFECT, \
                            BOW_EFFECT, SPEAR_EFFECT


def test_from_string_potion_type():
    pl = Potion.from_string('pl')
    pf = Potion.from_string('pf')
    po = Potion.from_string('po')
    assert pl.__eq__(PotionLife())
    assert pf.__eq__(PotionForce())
    assert po.__eq__(PotionPoison())

def test_from_string_weapon_type():
    sw = Weapon.from_string('sw')
    sp = Weapon.from_string('sp')
    wo = Weapon.from_string('wo')
    assert sw.__eq__(Sword())
    assert sp.__eq__(Spear())
    assert wo.__eq__(Bow())

# tests apply_effect potion
def test_apply_effect_potion_force_life_poison():
    # Potion force
    t0 = Tribute()
    potion_force = PotionForce()
    potion_force.apply_effect(t0)
    assert t0.force == (FORCE_DEFAULT + POTION_FORCE)

    t0.force = 30
    potion_force.apply_effect(t0)
    assert t0.force == 35

    # Potion life
    t1 = Tribute()
    t1.max_life = 100
    potion_life = PotionLife()
    potion_life.apply_effect(t1)
    assert t1.life == (LIFE_DEFAULT + POTION_LIFE)

    t1.life = 91
    t1.max_life = 100
    potion_life.apply_effect(t1)
    assert t1.life == 100

    t1.life = 100
    t1.max_life = 100
    potion_life.apply_effect(t1)
    assert t1.life == 100

    # Potion poison
    t2 = Tribute()
    poison = PotionPoison()
    poison.apply_effect(t2)
    assert t2.life == (LIFE_DEFAULT - POTION_POISON)

    t2.life = 3
    poison.apply_effect(t2)
    assert t2.is_dead() == True


# testing create_potion
def test_create_potion_force_life_poison():
    potion_force = PotionForce()
    num_potion_force = 10
    potion_force.create_potion(num_potion_force)
    assert potion_force.get_cant_items() == num_potion_force

    potion_life = PotionLife()
    num_potion_life = 25
    potion_life.create_potion(num_potion_life)
    assert potion_life.get_cant_items() == num_potion_life

    potion_poison = PotionPoison()
    num_potion_poison = 5
    potion_poison.create_potion(num_potion_poison)
    assert potion_poison.get_cant_items() == num_potion_poison


# testing apply_effect weapon
def test_apply_effect_weapon_sword_spear_bow():
    t0 = Tribute()
    sword = Sword()
    sword.apply_effect(t0)
    assert t0.force == FORCE_DEFAULT + SWORD_EFFECT
    assert t0.weapon == True
    with pytest.raises(ValueError):
        sword.apply_effect(t0)

    t1 = Tribute()
    spear = Spear()
    spear.apply_effect(t1)
    assert t1.range == 2
    assert t1.force == FORCE_DEFAULT + SPEAR_EFFECT
    assert t1.weapon == True
    with pytest.raises(ValueError):
        spear.apply_effect(t1)

    t1.force = 5
    t1.weapon = False
    spear.apply_effect(t1)
    assert t1.force == FORCE_DEFAULT + SPEAR_EFFECT

    t2 = Tribute()
    bow = Bow()
    bow.apply_effect(t2)
    assert t1.range == 3
    assert t2.force == FORCE_DEFAULT + BOW_EFFECT
    assert t2.weapon == True
    with pytest.raises(ValueError):
        bow.apply_effect(t2)

    t2.force = 15
    t2.weapon = False
    bow.apply_effect(t2)
    assert t2.force == 15 + BOW_EFFECT


# testing create_weapon
def test_create_weapon_sword_spear_bow():
    sword = Sword()
    sword.create_weapon(15)
    assert sword.cant_items == 15

    spear = Spear()
    spear.create_weapon(10)
    assert spear.cant_items == 10

    bow = Bow()
    bow.create_weapon(17)
    assert bow.cant_items == 17


def test_potion_life_get_pos():
    pl = PotionLife()
    pl.pos = (1, 1)
    res = pl.get_pos()
    assert res.__eq__((1, 1))


def test_weapon_sword_get_pos():
    sw = Sword()
    sw.pos = (3, 2)
    res = sw.get_pos()
    assert res.__eq__((3, 2))
