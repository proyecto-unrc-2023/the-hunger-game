import pytest

from game.logic.board import Board
from game.logic.item import Weapon, Potion
from game.logic.cell import Cell, State
from game.logic.tribute import Tribute
from game.logic.district import District


@pytest.fixture
def board():
    return Board(2, 2)


def test_initial_board(board: Board):
    assert board.rows == 2
    assert board.columns == 2
    assert board.get_element(0, 0).__eq__(Cell())
    assert board.get_element(0, 1).__eq__(Cell())
    assert board.get_element(1, 0).__eq__(Cell())
    assert board.get_element(1, 1).__eq__(Cell())


def test_put_one_live_tribute(board: Board):
    tribute = Tribute()
    board.put_tribute(1, 0, tribute)
    assert board.get_element(0, 0).get_state() == State.FREE
    assert board.get_element(0, 1).get_state() == State.FREE
    assert board.get_element(1, 0).get_state() == State.TRIBUTE
    assert board.get_element(1, 1).get_state() == State.FREE


def test_put_tribute_fails(board: Board):
    tribute = Tribute()
    board.put_tribute(1, 0, tribute)
    with pytest.raises(ValueError):
        board.put_tribute(1, 0, tribute)


def test_empty_board_to_string(board: Board):
    tribute = Tribute()
    board.put_tribute(0, 1, tribute)
    res = board.__str__()
    expected = ' |t\n' \
               ' | '
    assert expected == res


def test_board_with_two_tributes_to_string(board: Board):
    tribute1 = Tribute()
    tribute2 = Tribute()
    board.put_tribute(0, 1, tribute1)
    board.put_tribute(1, 1, tribute2)
    res = board.__str__()
    expected = ' |t\n' \
               ' |t'
    assert expected == res


def test_4x4_board_with_two_tribute_to_string():
    board = Board(4, 4)
    tribute1 = Tribute()
    tribute2 = Tribute()
    board.put_tribute(2, 1, tribute1)
    board.put_tribute(3, 3, tribute2)
    res = board.__str__()
    expected = ' | | | \n' \
               ' | | | \n' \
               ' |t| | \n' \
               ' | | |t'
    assert expected == res


def test_2x4_board_to_string():
    board = Board(2, 4)
    res = board.__str__()
    expected = ' | | | \n' \
               ' | | | '
    assert expected == res


def test_2x2_board_to_string_with_tribute_weapon_potion():
    board = Board(2, 2)
    board.put_tribute(0, 1, Tribute())
    board.put_item(0, 0, Potion())
    board.put_item(1, 1, Weapon())
    res = board.__str__()
    expected = 'p|t\n' \
               ' |w'
    assert expected == res


def test_2x2_board_from_string():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)
    assert board.__str__() == board_str


def test_2x4_board_from_string():
    board_str = ' | | | \n' \
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
    board.put_tribute(0, 1, tribute1)
    assert (board.get_element(0, 1)).__str__() == 't'
    board.remove_tribute(tribute1)
    assert (board.get_element(0, 1)).__str__() == ' '


def test_3x3_board_distribute_tribute():
    board_str = ' | | \n' \
                ' | | '
    board = Board.from_string(board_str)
    distrito1 = District()
    distrito1.set_config(50, 5, 1, 1, 4)
    board.distribute_tributes(distrito1)
    tributes_count = 0
    for row in board.board:
        for cell in row:
            if cell.state == State.TRIBUTE:
                tributes_count += 1
    assert tributes_count == 4


def test_2x2_board_put_item_weapon_from_string():
    board_str = 'w| \n' \
                ' | '
    board = Board.from_string(board_str)
    assert board.get_element(0, 0).get_state() == State.ITEM
    weapon = board.get_element(0, 0).get_item()
    assert weapon.__str__() == 'w'


def test_2x2_board_put_item_potion_from_string():
    board_str = ' |p\n' \
                ' | '
    board = Board.from_string(board_str)
    assert board.get_element(0, 1).get_state() == State.ITEM
    weapon = board.get_element(0, 1).get_item()
    assert weapon.__str__() == 'p'


def test_2x2_board_put_item_and_remove_item(board: Board):
    weapon1 = Weapon()
    board.put_item(0, 1, weapon1)
    assert board.get_element(0, 1).__str__() == 'w'
    board.remove_item(weapon1)
    assert board.get_element(0, 1).__str__() == ' '


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


def test_2x2_board_valid_pos(board: Board):
    t1 = Tribute()
    board.put_tribute(0, 1, t1)
    board.put_tribute(1, 1, Tribute())
    board.put_tribute(1, 0, Tribute())

    assert board.valid_pos((0, 0)) is True
    assert board.valid_pos((0, 1)) is False
    assert board.valid_pos((1, 0)) is False
    assert board.valid_pos((1, 1)) is False


def test_get_adjacents_cells_with_adjacent_cells():
    board = Board(3, 3)
    x, y = 1, 1
    adjacent_cells = board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 8
    assert board.get_element(0, 0) in adjacent_cells
    assert board.get_element(0, 1) in adjacent_cells
    assert board.get_element(0, 2) in adjacent_cells
    assert board.get_element(1, 0) in adjacent_cells
    assert board.get_element(1, 2) in adjacent_cells
    assert board.get_element(2, 0) in adjacent_cells
    assert board.get_element(2, 1) in adjacent_cells
    assert board.get_element(2, 2) in adjacent_cells


def test_get_adjacents_cells_with_boundary():
    board = Board(3, 3)
    x, y = 0, 0
    adjacent_cells = board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 3
    assert board.get_element(0, 1) in adjacent_cells
    assert board.get_element(1, 0) in adjacent_cells
    assert board.get_element(1, 1) in adjacent_cells


def test_get_adjacents_cells_with_cells_state_tribute():
    board = Board(3, 3)
    x, y = 1, 1
    board.put_tribute(1, 0, Tribute())
    board.put_tribute(0, 1, Tribute())
    board.put_tribute(1, 1, Tribute())
    adjacent_cells = board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 8
    assert board.get_element(0, 0) in adjacent_cells
    assert board.get_element(0, 1) in adjacent_cells
    assert board.get_element(0, 2) in adjacent_cells
    assert board.get_element(1, 0) in adjacent_cells
    assert board.get_element(1, 2) in adjacent_cells
    assert board.get_element(2, 0) in adjacent_cells
    assert board.get_element(2, 1) in adjacent_cells
    assert board.get_element(2, 2) in adjacent_cells


def test_get_adjacents_cells_with_invalid_coordinates(board: Board):
    board = Board(3, 3)
    x, y = -1, -1
    with pytest.raises(ValueError):
        board.get_adjacents_cells(x, y)

    # Test on a 3x3 board with invalid coordinates (beyond board size)
    x, y = 3, 3
    with pytest.raises(ValueError):
        board.get_adjacents_cells(x, y)



def test_get_free_adjacents_empty_board(board: Board):
    x, y = 0, 0
    free_adjacents = board.get_free_adjacents_cells(x, y)
    assert len(free_adjacents) == 3


def test_3x3_board_get_free_adjacents_empty_board():
    board = Board(3, 3)
    x, y = 1, 1
    free_adjacents = board.get_free_adjacents_cells(x, y)
    assert len(free_adjacents) == 8
    for cell in free_adjacents:
        assert cell.get_state() == State.FREE


def test_3x3_board_get_free_adjacents_some_adjacent_cells_occupied():
    board = Board(3, 3)
    x, y = 1, 1
    board.get_element(0, 1).put_tribute(Tribute())
    board.get_element(1, 0).put_tribute(Tribute())
    free_adjacents = board.get_free_adjacents_cells(x, y)
    assert len(free_adjacents) == 6
    for cell in free_adjacents:
        assert cell.get_state() == State.FREE


def test_get_free_adjacents_out_of_range(board: Board):
    x, y = -1, 0
    with pytest.raises(ValueError):
        board.get_free_adjacents_cells(x, y)


def test_get_free_adjacents_positions_valid_position():
    board = Board(3, 3)
    x, y = 1, 1
    free_positions = board.get_free_adjacents_positions(x, y)
    assert len(free_positions) == 8
    assert (0, 1) in free_positions
    assert (1, 0) in free_positions
    assert (1, 2) in free_positions
    assert (2, 1) in free_positions
    assert (0, 0) in free_positions
    assert (0, 2) in free_positions
    assert (2, 0) in free_positions
    assert (2, 2) in free_positions


def test_get_free_adjacents_positions_boundary_positions():
    board = Board(3, 3)

    # Esquina superior izquierda
    x, y = 0, 0
    free_positions = board.get_free_adjacents_positions(x, y)
    assert len(free_positions) == 3

    # Esquina inferior Derecha
    x, y = 2, 2
    free_positions = board.get_free_adjacents_positions(x, y)
    assert len(free_positions) == 3


def test_fill_board_with_tributes(board: Board):
    tribute1 = Tribute()
    tribute2 = Tribute()
    tribute3 = Tribute()
    tribute4 = Tribute()
    tributes = [tribute2, tribute3, tribute4]
    board.put_tribute(0, 0, tribute1)

    for tribute in tributes:
        x, y = board.random_choice(tribute1)
        board.put_tribute(x, y, tribute)

    board_str = 't|t\n' \
                't|t'
    board1 = board.__str__()
    assert board_str == board1
    # chequear si estan realmente todas ocupadas
    assert board.get_element(0, 0).get_state() == board.get_element(0, 1).get_state() == State.TRIBUTE
    assert board.get_element(1, 0).get_state() == board.get_element(1, 1).get_state() == State.TRIBUTE


def test_fill_board_with_tributes_avoid_occupied_cells():
    board = Board(3, 3)
    tribute1 = Tribute()
    board.put_tribute(1, 1, tribute1)

    tributes = [Tribute() for _ in range(7)]  # crear 7 tributes

    if board.get_free_adjacents_positions(1, 1):
        for tribute in tributes:
            x, y = board.random_choice(tribute1)
            assert board.get_element(x, y).get_state() == State.FREE
            board.put_tribute(x, y, tribute)
            assert board.get_element(x, y).get_state() == State.TRIBUTE
            assert (x, y) not in board.random_choice(tribute1)
    else:
        assert not tributes


def test_move_to_random():
    board = Board(3, 3)
    tribute = Tribute()
    board.put_tribute(1, 1, tribute)
    initial_pos = board.get_pos(tribute)
    board.move_to_random(tribute)
    new_pos = board.get_pos(tribute)
    assert board.get_element(initial_pos[0], initial_pos[1]).get_state() == State.FREE
    assert initial_pos != new_pos
    assert board.get_element(new_pos[0], new_pos[1]).get_state() == State.TRIBUTE
    assert tribute.pos == new_pos
    assert initial_pos != new_pos


def test_move_to():
    board = Board(3, 3)
    tribute = Tribute()
    board.put_tribute(1, 1, tribute)
    initial_pos = board.get_pos(tribute)
    x, y = 0, 2
    board.move_to(x, y, tribute)
    new_pos = board.get_pos(tribute)
    assert board.get_element(initial_pos[0], initial_pos[1]).get_state() == State.FREE
    assert initial_pos != new_pos
    assert (new_pos[0], new_pos[1]) == (x, y)
    assert board.get_element(x, y).get_state() == State.TRIBUTE
    assert tribute.pos == new_pos

def test_move_closer_to():
    board = Board(5, 5)
    tribute = Tribute()
    board.put_tribute(1, 1, tribute)
    (x, y) = board.move_closer_to(1, 2, tribute)
    board.move_to(x, y, tribute)
    assert tribute.pos == (1,2)
    (x, y) = board.move_closer_to(4, 4, tribute)
    board.move_to(x, y, tribute)
    (x, y) = board.move_closer_to(4, 4, tribute)
    board.move_to(x, y, tribute)
    (x, y) = board.move_closer_to(4, 4, tribute)
    board.move_to(x, y, tribute)
    assert tribute.pos == (4,4)
def test_get_adjacent_positions():
    board = Board(4, 4)

    # Prueba una posición en el centro del tablero (2, 2)
    adjacent_positions = board.get_adjacent_positions(2, 2)
    expected_positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
    assert adjacent_positions == expected_positions

    # Prueba una posición en la esquina superior izquierda (0, 0)
    adjacent_positions = board.get_adjacent_positions(0, 0)
    expected_positions = [(0, 1), (1, 0), (1, 1)]
    assert adjacent_positions == expected_positions

    # Prueba una posición en la esquina inferior derecha (3, 3)
    adjacent_positions = board.get_adjacent_positions(3, 3)
    expected_positions = [(2, 2), (2, 3), (3, 2)]
    assert adjacent_positions == expected_positions

    # Prueba una posición en el borde derecho (1, 3)
    adjacent_positions = board.get_adjacent_positions(1, 3)
    expected_positions = [(0, 2), (0, 3), (1, 2), (2, 2), (2, 3)]
    assert adjacent_positions == expected_positions

    # Prueba una posición en el borde izquierdo (2, 0)
    adjacent_positions = board.get_adjacent_positions(2, 0)
    expected_positions = [(1, 0), (1, 1), (2, 1), (3, 0), (3, 1)]
    assert adjacent_positions == expected_positions

    # Prueba una posición en el borde inferior (3, 1)
    adjacent_positions = board.get_adjacent_positions(3, 1)
    expected_positions = [(2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]
    assert adjacent_positions == expected_positions

