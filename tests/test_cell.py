import pytest
from game.logic.cell import Cell, State
from game.logic.tribute import Tribute
from game.logic.item import Item, Potion, Weapon


def test_cell_initial_state():
    cell = Cell()
    assert cell.get_state() == State.FREE
    with pytest.raises(ValueError):
        cell.get_item()
    with pytest.raises(ValueError):
        cell.get_tribute()


def test_put_and_remove_tribute():
    cell = Cell()
    tribute = Tribute()
    cell.put_tribute(tribute)
    assert cell.get_state() == State.TRIBUTE
    assert cell.get_tribute() == tribute
    cell.remove_tribute()
    assert cell.get_state() == State.FREE
    with pytest.raises(ValueError):
        cell.get_tribute()


def test_put_and_remove_item():
    cell = Cell()
    item = Item()
    cell.put_item(item)
    assert cell.get_state() == State.ITEM
    assert cell.get_item() == item
    cell.remove_item()
    assert cell.get_state() == State.FREE
    with pytest.raises(ValueError):
        cell.get_item()


def test_put_item_on_top_of_tribute():
    cell = Cell()
    tribute = Tribute()
    cell.put_tribute(tribute)
    item = Item()
    with pytest.raises(ValueError):
        cell.put_item(item)


def test_put_tribute_on_top_of_item():
    cell = Cell()
    item = Item()
    cell.put_item(item)
    assert cell.get_item() == item


def test_remove_item_when_no_item():
    cell = Cell()
    with pytest.raises(ValueError):
        cell.remove_item()


def test_remove_tribute_when_no_tribute():
    cell = Cell()
    with pytest.raises(ValueError):
        cell.remove_tribute()


def test_item_and_tribute_interaction():
    cell = Cell()
    item = Item()
    tribute = Tribute()

    # Coloca un ítem y verifica que esté en la celda
    cell.put_item(item)
    assert cell.get_state() == State.ITEM
    assert cell.get_item() == item

    # Intenta colocar un tributo y verifica que se cambie el state
    cell.put_tribute(tribute)
    assert cell.get_item() == item
    assert cell.get_tribute() == tribute
    assert cell.state == State.TRIBUTE
    # Elimina el ítem y verifica que la celda aun tiene tribute 
    cell.remove_item()
    assert cell.get_state() == State.TRIBUTE
    with pytest.raises(ValueError):
        cell.get_item()

    # Intenta colocar un ítem y verifica que se lance una excepción
    with pytest.raises(ValueError):
        cell.put_item(item)

    # Elimina el tributo y verifica que la celda vuelva a estar libre
    cell.remove_tribute()
    assert cell.get_state() == State.FREE
    with pytest.raises(ValueError):
        cell.get_tribute()


def test_string_representation():
    cell = Cell()
    assert str(cell) == '  '

    weapon = Weapon()
    cell.put_item(weapon)
    assert str(cell) == weapon.__str__()

    potion = Potion()
    cell.remove_item()
    cell.put_item(potion)
    assert str(cell) == potion.__str__()

    tribute = Tribute()
    cell.put_tribute(tribute)
#    assert str(cell) == tribute.__str__()
