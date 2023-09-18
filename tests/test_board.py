import pytest

from game.logic.board import Board
from game.logic.tribute import DeadTribute, LiveTribute


#@pytest.fixture(scope='module')
#def complex_object():
#    # Create an object that is costly to initialize
#    return ComplexObject(...)



@pytest.fixture
def board():
    return Board(2, 2)


def test_initial_board(board):
    assert board.rows == 2
    assert board.columns == 2
    assert board.get_tribute(0, 0).__eq__(DeadTribute())
    assert board.get_tribute(0, 1).__eq__(DeadTribute())
    assert board.get_tribute(1, 0).__eq__(DeadTribute())
    assert board.get_tribute(1, 1).__eq__(DeadTribute())


def test_put_one_live_tribute(board):
    board.put_live_tribute(1, 0)
    assert board.get_tribute(0, 0).__eq__(DeadTribute())
    assert board.get_tribute(0, 1).__eq__(DeadTribute())
    assert board.get_tribute(1, 0).__eq__(LiveTribute())
    assert board.get_tribute(1, 1).__eq__(DeadTribute())


def test_put_live_tribute_fails(board):
    board.put_live_tribute(1, 0)
    with pytest.raises(ValueError):
        board.put_live_tribute(1, 0)


def test_empty_board_to_string(board):
    res = board.__str__()
    expected = ' | \n' \
               ' | '
    assert expected == res

def test_board_with_two_tributes_to_string(board):
    board.put_live_tribute(0, 1)
    board.put_live_tribute(1, 1)
    res = board.__str__()
    expected = ' |t\n' \
               ' |t'
    assert expected == res

def test_empty_board_to_string(board):
    res = board.__str__()
    expected = ' | \n' \
               ' | '
    assert expected == res


# def test_4x4_board_with_two_tribute_to_string():
#     board = Board(4, 4)
#     res = board.__str__()
#     expected = ' | | | \n'\
#                ' | | | \n'\
#                ' | | | \n'\
#                ' | | | '
#     assert expected == res


# def test_2x4_board__to_string():
#     board = Board(2, 4)
#     res = board.__str__()
#     expected = ' | | | \n'\
#                ' | | | '
#     assert expected == res


# def test_2x2_board_from_string():
#     board_str = ' | \n' \
#                 ' | '
#     board = Board.from_string(board_str)
#     assert board.__str__() == board_str

# def test_2x4_board_from_string():
#     board_str = ' | | | \n'\
#                 ' | | | '
#     board = Board.from_string(board_str)
#     assert board.__str__() == board_str

