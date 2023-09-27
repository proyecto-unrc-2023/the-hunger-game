import pytest

from game.logic.tribute import LiveTribute
from game.logic.item import Item, Potion, Weapon

def test_create_potion_from_str():
    res = Item.from_string('p')
    
    assert res.__eq__(Potion())

def test_create_weapon_from_str():
    res = Item.from_string('w')
    
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
    
def test_potion_get_pos():
    potion = Potion()
    potion.pos = (1,1)
    
    res = potion.get_pos()
    assert res.__eq__((1,1))
    
def test_weapon_get_pos():
    weapon = Weapon()
    weapon.pos = (3,2)
    
    res = weapon.get_pos()
    assert res.__eq__((3,2))
    
def test_potion_set_pos():
    potion = Potion()
    potion.set_pos((1,2))
    
    res = potion.pos
    assert res.__eq__((1,2))
    
def test_weapon_get_pos():
    weapon = Weapon()
    weapon.set_pos = (2,2)
    
    res = weapon.pos
    assert res.__eq__((2,2))