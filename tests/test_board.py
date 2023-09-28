import pytest

from game.logic.board import Board
from game.logic.item import Weapon, Potion
from game.logic.cell import Cell, State
from game.logic.tribute import Tribute

@pytest.fixture
def board():
    return Board(2, 2)


def test_initial_board(board):
    assert board.rows == 2
    assert board.columns == 2
    assert board.get_element(0, 0).__eq__(Cell())
    assert board.get_element(0, 1).__eq__(Cell())
    assert board.get_element(1, 0).__eq__(Cell())
    assert board.get_element(1, 1).__eq__(Cell())


def test_put_one_live_tribute(board):
    tribute = Tribute()
    board.put_tribute(1, 0, tribute)
    assert board.get_element(0, 0).get_state() == State.FREE
    assert board.get_element(0, 1).get_state() == State.FREE
    assert board.get_element(1, 0).get_state() == State.TRIBUTE
    assert board.get_element(1, 1).get_state() == State.FREE

def test_put_tribute_fails(board):
    tribute = Tribute()
    board.put_tribute(1, 0, tribute)
    with pytest.raises(ValueError):
        board.put_tribute(1, 0, tribute)

def test_empty_board_to_string(board):
    res = board.__str__()
    expected = ' | \n' \
               ' | '
    assert expected == res

def test_board_with_two_tributes_to_string(board):
    tribute1 = Tribute()
    tribute2 = Tribute()
    board.put_tribute(0, 1,tribute1)
    board.put_tribute(1, 1,tribute2)
    res = board.__str__()
    expected = ' |t\n' \
               ' |t'
    assert expected == res
    
def test_4x4_board_with_two_tribute_to_string():
     board = Board(4, 4)
     res = board.__str__()
     expected = ' | | | \n'\
                ' | | | \n'\
                ' | | | \n'\
                ' | | | '
     assert expected == res

def test_2x4_board__to_string():
     board = Board(2, 4)
     res = board.__str__()
     expected = ' | | | \n'\
                ' | | | '
     assert expected == res

def test_2x2_board_from_string():
     board_str = ' | \n' \
                 ' | '
     board = Board.from_string(board_str)
     assert board.__str__() == board_str

def test_2x4_board_from_string():
     board_str = ' | | | \n'\
                 ' | | | '
     board = Board.from_string(board_str)
     assert board.__str__() == board_str

def test_2x2_board_get_pos():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_pos(tribute1) == (0, 1)

def test_2x2_board_put_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_element(0, 1).get_state() == State.TRIBUTE
    tribute2 = board.get_element(0, 1).get_tribute()
    assert tribute2.__str__() == 't'
    
def test_2x2_board_put_tribute_and_remove_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_element(0, 1).get_state() == State.TRIBUTE
    board.remove_tribute(tribute1)
    assert board.get_element(0, 1).get_state() == State.FREE
    

def test_2x2_board_remove_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)
    tribute1 = Tribute()
    board.put_tribute(0,1,tribute1)
    assert (board.get_element(0,1)).__str__() == 't'
    board.remove_tribute(tribute1)
    assert (board.get_element(0,1)).__str__() == ' '

    
#completar este cuando este distric y tributes
#necesito district y tributes... completar
#def test_3_3_board_distribute_tribute():
#    board_str = ' |w| \n' \
#                ' | | '
#    board = Board.from_string(board_str)
#    distrito1 = District()
#    for i in range(district1)
#        board.put_tribute(district.tibute[i])


def test_2x2_board_put_item_weapon():
    board_str = 'w| \n' \
                ' | '
    board = Board.from_string(board_str)
    assert board.get_element(0, 0).get_state() == State.ITEM
    weapon = board.get_element(0, 0).get_item()
    assert weapon.__str__() == 'w'

def test_2x2_board_put_item_potion():
    board_str = ' |p\n' \
                ' | '
    board = Board.from_string(board_str)
    assert board.get_element(0, 1).get_state() == State.ITEM
    weapon = board.get_element(0, 1).get_item()
    assert weapon.__str__() == 'p'

 
#necesito item.pos    
#def test_2x2_board_put_item_and_remove_item(board):
#    weapon1 = Weapon()
#    board.put_item(0,1, weapon1)
#    assert board.get_element(0,1).__str__() == 'w'
#    board.remove_item(weapon1)
#    assert board.get_element(0,1).__str__() == ' '

def test_2x2_board_random_pos():
    board_str = 't|t\n' \
                ' |t'
    board = Board.from_string(board_str)
    pos = board.random_pos()
    assert pos == (1, 0) 

    
def test_2x2_board_get_pos_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_pos(tribute1) == (0, 1)