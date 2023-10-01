import pytest

from game.logic.game_logic import GameLogic
from game.logic.board import Board
from game.logic.item import Potion, Weapon
from game.logic.tribute import Tribute

def test_tribute_vision_pos():
    game = GameLogic()
    game.new_game(7,7)
    t1 = Tribute()
    t1.pos = (3,3)
        
    visible_positions = game.tribute_vision_pos(t1)
    assert len(visible_positions) == 48
    for x in range(6):
      for y in range(6):
        if x != 3 and y != 3 :
            assert (x, y) in visible_positions
            assert (x, y) in visible_positions
            assert (x, y) in visible_positions
            assert (x, y) in visible_positions
            assert (x, y) in visible_positions
            assert (x, y) in visible_positions
            assert (x, y) in visible_positions

def test_tribute_vision_pos_with_tribute_in_border():
    game = GameLogic()
    game.new_game(7,7)
    t1 = Tribute()
    t1.pos = (0,0)
        
    visible_positions = game.tribute_vision_pos(t1)
    assert len(visible_positions) == 15
    assert (0, 1) in visible_positions
    assert (0, 2) in visible_positions
    assert (0, 3) in visible_positions
    assert (1, 0) in visible_positions
    assert (1, 1) in visible_positions
    assert (1, 2) in visible_positions
    assert (1, 3) in visible_positions
    assert (2, 0) in visible_positions
    assert (2, 1) in visible_positions
    assert (2, 2) in visible_positions
    assert (2, 3) in visible_positions
    assert (3, 0) in visible_positions
    assert (3, 1) in visible_positions
    assert (3, 2) in visible_positions
    assert (3, 3) in visible_positions


def test_tribute_vision_cells_with_a_cells():
    game = GameLogic()
    game.new_game(3,3)
    x, y = 1, 1
    tribute1 = Tribute()
    game.board.put_tribute(1,1, tribute1)
    tribute_vision_cells = game.tribute_vision_cells(tribute1)
    assert len(tribute_vision_cells) == 8
    assert game.board.get_element(0, 0) in tribute_vision_cells
    assert game.board.get_element(0, 1) in tribute_vision_cells
    assert game.board.get_element(0, 2) in tribute_vision_cells
    assert game.board.get_element(1, 0) in tribute_vision_cells
    assert game.board.get_element(1, 2) in tribute_vision_cells
    assert game.board.get_element(2, 0) in tribute_vision_cells
    assert game.board.get_element(2, 1) in tribute_vision_cells
    assert game.board.get_element(2, 2) in tribute_vision_cells

def test_tribute_vision_cells_with_boundary():
    game = GameLogic()
    game.new_game(3,3)
    x, y = 0, 0
    adjacent_cells = game.board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 3
    assert game.board.get_element(0, 1) in adjacent_cells
    assert game.board.get_element(1, 0) in adjacent_cells
    assert game.board.get_element(1, 1) in adjacent_cells

def test_tribute_vision_cells_with_cells_state_tribute():
    game = GameLogic()
    game.new_game(3,3)
    x, y = 1, 1
    game.board.put_tribute(1, 0, Tribute())
    game.board.put_tribute(0, 1, Tribute())
    game.board.put_tribute(1, 1, Tribute())
    adjacent_cells = game.board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 8
    assert game.board.get_element(0, 0) in adjacent_cells
    assert game.board.get_element(0, 1) in adjacent_cells
    assert game.board.get_element(0, 2) in adjacent_cells
    assert game.board.get_element(1, 0) in adjacent_cells
    assert game.board.get_element(1, 2) in adjacent_cells
    assert game.board.get_element(2, 0) in adjacent_cells
    assert game.board.get_element(2, 1) in adjacent_cells
    assert game.board.get_element(2, 2) in adjacent_cells
#-------

def test_get_adjacents_cells_with_invalid_coordinates():
    board = Board(3, 3)
    x, y = -1, -1
    with pytest.raises(ValueError):
        board.get_adjacents_cells(x, y)

    # Test on a 3x3 board with invalid coordinates (beyond board size)
    x, y = 3, 3
    with pytest.raises(ValueError):
        board.get_adjacents_cells(x, y)

def test_get_tribute_vision_cells_ocupped_order_by_closeness():
    game = GameLogic()
    game.new_game(7, 7)
    t1 = Tribute()
    t2 = Tribute()
    w1 = Weapon()
    p1 = Potion()
    p2 = Potion()
    game.board.put_tribute(2, 2, t1)
    game.board.put_tribute(1, 1, t2)
    game.board.put_item(5, 6, w1)
    game.board.put_item(6, 6, p1)
    game.board.put_item(5, 5, p2)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1) == (1,1)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t2) == (2,2)

    
