import pytest

from game.logic.tribute import LiveTribute
from game.logic.object import Object, Potion, Weapon

def test_create_not_used_potion_from_str():
    res = Object.from_string('p')
    
    assert res.__eq__(Potion())
    
def test_create_used_potion_from_str():
    res = Object.from_string('-p')

    assert res.__eq__(Potion())

def test_create_not_used_weapon_from_str():
    res = Object.from_string('w')
    
    assert res.__eq__(Weapon())

def test_create_used_weapon_from_str():
    res = Object.from_string('-w')
    
    assert res.__eq__(Weapon())
    
def test_potion_applies_efect():
    tribute = LiveTribute()
    tribute.life = 75
    
    Potion.applies_efects(tribute)
    
    assert tribute.life.__eq__(80)
    
def test_weapon_applies_efect():
    tribute = LiveTribute()
    tribute.force = 6
    
    Weapon.applies_efects(tribute)
    
    assert tribute.force.__eq__(7)
    