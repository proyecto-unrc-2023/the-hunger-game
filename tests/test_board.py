import pytest

from game.logic.board import Board
from game.logic.item import Weapon, Sword, Spear, Bow, Potion, PotionLife, PotionForce, PotionPoison
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


def test_from_string():
    expected = '  |n0|t1\n' \
               'a1|b0|a0\n' \
               'a2|n1|b2'
    board_obj = Board.from_string(expected)[0]  # Crea el objeto Board a partir de la cadena
    print(board_obj.get_element(0, 1).get_tribute().name)
    res = str(board_obj.__str__())  # Obtiene la representación de cadena del objeto Board
    assert expected == res


def test_put_tribute_fails(board: Board):
    tribute = Tribute()
    board.put_tribute(1, 0, tribute)
    with pytest.raises(ValueError):
        board.put_tribute(1, 0, tribute)


def test_empty_board_to_string(board: Board):
    tribute = Tribute()
    board.put_tribute(0, 1, tribute)
    t0 = Tribute()
    t0.set_config_parameters(50, 5, 3, 0)
    t0.name = 't0'
    board.put_tribute(1, 1, t0)
    res = board.__str__()
    expected = '  |t \n' \
               '  |t0'
    assert expected == res
    t1 = Tribute()
    t1.set_config_parameters(50, 5, 3, 1)
    t1.name = 't1'
    board.put_tribute(1, 0, t1)
    res = board.__str__()
    expected = '  |t \n' \
               't1|t0'
    assert expected == res
    assert board.get_element(1, 0).get_tribute() == t1


def test_board_with_two_tributes_to_string(board: Board):
    tribute1 = Tribute()
    tribute2 = Tribute()
    board.put_tribute(0, 1, tribute1)
    board.put_tribute(1, 1, tribute2)
    res = board.__str__()
    expected = '  |t \n' \
               '  |t '
    assert expected == res


def test_4x4_board_with_two_tribute_to_string():
    board = Board(4, 4)
    tribute1 = Tribute()
    tribute2 = Tribute()
    board.put_tribute(2, 1, tribute1)
    board.put_tribute(3, 3, tribute2)
    res = board.__str__()
    expected = '  |  |  |  \n' \
               '  |  |  |  \n' \
               '  |t |  |  \n' \
               '  |  |  |t '
    assert expected == res


def test_2x2_board_to_string_with_tribute_weapon_potion():
    board = Board(2, 2)
    board.put_tribute(0, 1, Tribute())
    board.put_item(0, 0, Potion())
    board.put_item(1, 1, Weapon())
    res = board.__str__()
    expected = 'p |t \n' \
               '  |w '
    assert expected == res


def test_2x2_board_from_string():
    board_str = 't3|t2\n' \
                't4|t1'
    board = Board.from_string(board_str)[0]
    assert board.__str__() == board_str
    t1 = board.get_element(1, 1).get_tribute()
    t3 = board.get_element(0, 0).get_tribute()
    t2 = board.get_element(0, 1).get_tribute()
    assert t1.life == 50
    assert t1.district == 1
    assert t2.district == 2
    assert t3.district == 3


def test_2x4_board_from_string():
    board_str = '  |  |  |  \n' \
                '  |  |  |  '
    board = Board.from_string(board_str)[0]
    assert board.__str__() == board_str


def test_2x2_board_get_pos():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)[0]
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_pos(tribute1) == (0, 1)


def test_2x2_board_put_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)[0]
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_element(0, 1).get_state() == State.TRIBUTE
    tribute2 = board.get_element(0, 1).get_tribute()
    assert tribute2.__str__() == 't '


def test_2x2_board_put_tribute_and_remove_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)[0]
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_element(0, 1).get_state() == State.TRIBUTE
    board.remove_tribute(tribute1)
    assert board.get_element(0, 1).get_state() == State.FREE


def test_2x2_board_remove_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)[0]
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert (board.get_element(0, 1)).__str__() == 't '
    board.remove_tribute(tribute1)
    assert (board.get_element(0, 1)).__str__() == '  '


def test_3x3_board_distribute_tribute():
    board_str = ' | | \n' \
                ' | | '
    board = Board.from_string(board_str)[0]
    distrito1 = District()
    distrito1.set_config(50, 5, 3, 0, 4)
    board.distribute_tributes(distrito1)
    tributes_count = 0
    for row in board.board:
        for cell in row:
            if cell.state == State.TRIBUTE:
                tributes_count += 1
    assert tributes_count == 4


def test_2x2_board_put_item_weapon_from_string():
    board_str = 'sp|  \n' \
                '  |  '
    board = Board.from_string(board_str)[0]
    assert board.get_element(0, 0).get_state() == State.ITEM
    spear = board.get_element(0, 0).get_item()
    assert spear.__str__() == 'sp'
    board2_str = 'sw|  \n' \
                 '  |  '
    board2_str = Board.from_string(board2_str)[0]
    assert board2_str.get_element(0, 0).get_state() == State.ITEM
    sword = board2_str.get_element(0, 0).get_item()
    assert sword.__str__() == 'sw'
    board3_str = 'wo|  \n' \
                 '  |  '
    board3_str = Board.from_string(board3_str)[0]
    assert board3_str.get_element(0, 0).get_state() == State.ITEM
    bow = board3_str.get_element(0, 0).get_item()
    assert bow.__str__() == 'wo'


def test_2x2_board_put_item_potion_from_string():
    board_str = '  |pf \n' \
                '  |  '
    board = Board.from_string(board_str)[0]
    assert board.get_element(0, 1).get_state() == State.ITEM
    weapon = board.get_element(0, 1).get_item()
    assert weapon.__str__() == 'pf'


def test_2x2_board_put_item_and_remove_item(board: Board):
    weapon1 = Weapon()
    board.put_item(0, 1, weapon1)
    assert board.get_element(0, 1).__str__() == 'w '
    board.remove_item(weapon1)
    assert board.get_element(0, 1).__str__() == '  '


def test_2x2_board_random_pos():
    board_str = 'n|n\n' \
                ' |a1'
    board = Board.from_string(board_str)[0]
    pos = board.random_pos()
    assert pos == (1, 0)


def test_2x2_board_get_pos_tribute():
    board_str = ' | \n' \
                ' | '
    board = Board.from_string(board_str)[0]
    tribute1 = Tribute()
    board.put_tribute(0, 1, tribute1)
    assert board.get_pos(tribute1) == (0, 1)


def test_2x2_board_valid_pos(board: Board):
    t1 = Tribute()
    board.put_tribute(0, 1, t1)
    board.put_item(1, 0, Weapon())

    assert board.valid_pos((0, 0)) is True
    assert board.valid_pos((0, 1)) is False
    assert board.valid_pos((1, 0)) is True
    assert board.valid_pos((1, 1)) is True


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
    free_adjacents = board.get_free_adjacents_positions(x, y)
    expected_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

    assert len(free_adjacents) == len(expected_positions)
    for pos in expected_positions:
        assert pos in free_adjacents


def test_3x3_board_get_free_adjacents_some_adjacent_cells_occupied():
    board = Board(7, 7)
    x, y = 3, 3
    board.get_element(2, 3).put_tribute(Tribute())
    board.get_element(2, 2).put_tribute(Tribute())
    board.get_element(2, 0).put_item(Weapon())
    free_adjacents = board.get_free_adjacents_cells(x, y)
    assert len(free_adjacents) == 6
    for cell in free_adjacents:
        assert (cell.get_state() == State.FREE or cell.get_state() == State.ITEM)


def test_3x3_board_get_free_adjacents_cells_expected():
    board = Board(7, 7)
    x, y = 3, 3
    board.get_element(0, 1).put_tribute(Tribute())
    board.get_element(2, 3).put_tribute(Tribute())
    board.get_element(2, 2).put_item(Weapon())
    free_adjacents = board.get_free_adjacents_cells(x, y)

    expected_positions = [(2, 2), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]

    assert len(free_adjacents) == len(expected_positions)

    for pos in expected_positions:
        cell = board.get_element(pos[0], pos[1])
        assert (cell.get_state() == State.FREE or cell.get_state() == State.ITEM)


def test_get_free_adjacents_out_of_range(board: Board):
    x, y = -1, 0
    with pytest.raises(ValueError):
        board.get_free_adjacents_cells(x, y)


def test_get_free_adjacents_positions_valid_position():
    board = Board(3, 3)
    x, y = 1, 1
    board.put_item(2, 2, Weapon())
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

    board_str = 't |t \n' \
                't |t '
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


def test_put_item_using_create_potion():
    board = Board(3, 3)
    potion_life = PotionLife()
    potion_force = PotionForce()
    potion_poison = PotionPoison()

    potion_life.create_potion(2)
    potion_force.create_potion(2)
    potion_poison.create_potion(3)

    board.put_item(0, 0, potion_life.items[0])
    board.put_item(1, 1, potion_life.items[1])

    board.put_item(2, 0, potion_force.items[0])
    board.put_item(2, 1, potion_force.items[1])

    board.put_item(0, 2, potion_poison.items[0])
    board.put_item(1, 2, potion_poison.items[1])
    board.put_item(2, 2, potion_poison.items[2])

    res = board.__str__()
    expected = 'pl|  |po\n' \
               '  |pl|po\n' \
               'pf|pf|po'
    assert expected == res
    board.remove_item(potion_life.items[0])
    res = board.__str__()
    expected = '  |  |po\n' \
               '  |pl|po\n' \
               'pf|pf|po'
    assert expected == res


def test_put_item_using_create_weapon():
    board = Board(3, 3)
    sword = Sword()
    spear = Spear()
    bow = Bow()

    sword.create_weapon(2)
    spear.create_weapon(1)
    bow.create_weapon(4)

    board.put_item(0, 1, sword.items[0])
    board.put_item(2, 0, sword.items[1])

    board.put_item(1, 2, spear.items[0])

    board.put_item(0, 0, bow.items[0])
    board.put_item(0, 2, bow.items[1])
    board.put_item(1, 1, bow.items[2])
    board.put_item(2, 2, bow.items[3])

    res = board.__str__()
    expected = 'wo|sw|wo\n' \
               '  |wo|sp\n' \
               'sw|  |wo'
    assert expected == res


def test_distribute_items_potions():
    board = Board(4, 4)
    potion_life = PotionLife()
    potion_force = PotionForce()
    potion_poison = PotionPoison()

    potion_life.create_potion(4)
    potion_force.create_potion(5)
    potion_poison.create_potion(3)

    board.distribute_items(potion_life)
    board.distribute_items(potion_force)
    board.distribute_items(potion_poison)

    count_potions = 0
    for row in board.board:
        for cell in row:
            if cell.state == State.ITEM:
                count_potions += 1

    assert count_potions == 12


def test_distribute_items_weapons():
    board = Board(4, 4)
    sword = Sword()
    spear = Spear()
    bow = Bow()

    sword.create_weapon(5)
    spear.create_weapon(5)
    bow.create_weapon(4)

    board.distribute_items(sword)
    board.distribute_items(spear)
    board.distribute_items(bow)

    count_weapons = 0
    for row in board.board:
        for cell in row:
            if cell.state == State.ITEM:
                count_weapons += 1

    assert count_weapons == 14
