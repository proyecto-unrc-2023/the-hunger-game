import pytest

from game.logic.cell import State, Cell
from game.logic.district import District
from game.logic.game_logic import GameLogic, GameMode
from game.logic.board import Board
from game.logic.item import Item, Potion, Weapon, WEAPON_EFFECT
from game.logic.tribute import Tribute
from game.logic.district import District


@pytest.fixture
def game():
    game = GameLogic()
    game.new_game(5, 5)
    t1 = Tribute()
    t2 = Tribute()
    t3 = Tribute()
    w1 = Weapon()
    p1 = Potion()
    game.board.put_tribute(2, 2, t1)
    game.board.put_tribute(1, 1, t2)
    game.board.put_tribute(3, 3, t3)
    game.board.put_item(4, 4, w1)
    game.board.put_item(4, 3, p1)
    return game


@pytest.fixture
def game2x2():
    game2x2 = GameLogic()
    game2x2.new_game(2, 2)
    district0 = District()
    district1 = District()
    t0 = Tribute()
    t1 = Tribute()
    district0.number_district = 0
    district1.number_district = 1

    game2x2.districts.append(district0)
    game2x2.districts.append(district1)
    t0.set_config_parameters(50, 20, 1, 0)
    t1.set_config_parameters(50, 20, 1, 1)
    game2x2.board.put_tribute(0, 0, t0)
    game2x2.board.put_tribute(0, 1, t1)
    district0.add_tribute(t0)
    district1.add_tribute(t1)
    return game2x2


def test_from_string():
    game = GameLogic()
    board_str = 't3|t2\n' \
                't4|t1'
    game.from_string(board_str)
    assert len(game.districts[1].tributes) == 1
    assert len(game.districts[2].tributes) == 1
    assert len(game.districts[3].tributes) == 1
    assert len(game.districts[4].tributes) == 1
    t1 = game.board.get_element(1, 1).get_tribute()
    game.remove_tribute(t1)
    assert len(game.districts[1].tributes) == 0


def test_put_neutral(game2x2):
    game2x2.put_neutral(1, 0)
    neutral = game2x2.board.get_element(1, 0).get_tribute()
    assert neutral.life == 50
    assert neutral.force == 5
    assert neutral.pos == (1, 0)
    assert neutral.district is None
    assert len(game2x2.neutrals) == 1


def test_remove_tribute(game2x2):
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    game2x2.remove_tribute(t1)
    assert game2x2.board.get_element(0, 0).get_state() == State.FREE
    assert not (t1 in game2x2.districts[t1.district].tributes)


def test_tribute_vision_pos():
    game = GameLogic()
    game.new_game(7, 7)
    t1 = Tribute()
    t1.pos = (3, 3)

    visible_positions = game.tribute_vision_pos(t1)
    assert len(visible_positions) == 48
    for x in range(6):
        for y in range(6):
            if x != 3 and y != 3:
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions
                assert (x, y) in visible_positions


def test_tribute_vision_pos_with_tribute_in_border():
    game = GameLogic()
    game.new_game(7, 7)
    t1 = Tribute()
    t1.pos = (0, 0)

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
    game.new_game(3, 3)
    x, y = 1, 1
    tribute1 = Tribute()
    game.board.put_tribute(1, 1, tribute1)
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
    game.new_game(8, 8)
    x, y = 0, 0
    adjacent_cells = game.board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 3
    assert game.board.get_element(0, 1) in adjacent_cells
    assert game.board.get_element(1, 0) in adjacent_cells
    assert game.board.get_element(1, 1) in adjacent_cells
    # Modifica el cuarto assert
    assert len([cell for cell in adjacent_cells if cell.get_pos() == (7, 7)]) == 0


def test_tribute_vision_cells_with_cells_state_tribute():
    game = GameLogic()
    game.new_game(3, 3)
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


def test_get_adjacents_cells_with_invalid_coordinates():
    board = Board(3, 3)
    x, y = -1, -1
    with pytest.raises(ValueError):
        board.get_adjacents_cells(x, y)

    # Test on a 3x3 board with invalid coordinates (beyond board size)
    x, y = 3, 3
    with pytest.raises(ValueError):
        board.get_adjacents_cells(x, y)


def test_get_tribute_closenes_with_neutral_weapon_potion_tribute():
    game = GameLogic()
    game.new_game(3, 3)
    t1 = Tribute()
    t2 = Tribute()
    neutro = Tribute()
    w = Weapon()
    p = Potion()
    t1.set_config_parameters(50, 5, 1, 1)
    t2.set_config_parameters(50, 5, 1, 2)
    game.board.put_tribute(1, 1, t1)
    game.board.put_tribute(0, 1, t2)  # //arriba
    game.board.put_item(2, 1, w)  # ABAJO
    game.board.put_item(1, 0, p)  # izquierda
    game.board.put_tribute(1, 2, neutro)  # derecha
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (2, 1)
    game.board.remove_item(w)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (1, 0)
    game.board.remove_item(p)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (1, 2)
    game.board.remove_tribute(neutro)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (0, 1)


def test_get_tribute_closeness_with_same_district():
    game = GameLogic()
    game.new_game(7, 7)
    t1 = Tribute()
    t2 = Tribute()
    t1.set_config_parameters(50, 5, 1, 1)
    t2.set_config_parameters(50, 5, 1, 1)
    game.board.put_tribute(3, 3, t1)
    game.board.put_tribute(3, 4, t2)
    p = Potion()
    game.board.put_item(5, 5, p)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (5, 5)


def test_tribute_vision_cells_ocupped_order_by_closeness_empty_board():
    game = GameLogic()
    game.new_game(5, 5)
    t1 = Tribute()
    game.board.put_tribute(2, 2, t1)
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1)
    assert result == False


def test_tribute_vision_cells_loseness_tributes_same_district2():
    game = GameLogic()
    game.new_game(2, 2)
    t0 = Tribute()
    t1 = Tribute()
    t0.set_config_parameters(40, 4, 4, 0)
    t1.set_config_parameters(40, 4, 4, 0)
    game.board.put_tribute(0, 0, t0)
    game.board.put_tribute(0, 1, t1)
    d0 = District()
    d0.add_tribute(t0)
    d0.add_tribute(t1)
    game.districts.append(d0)
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1)
    assert result is False


def test_tribute_vision_cells_ocupped_order_by_closeness_items_only():
    game = GameLogic()
    game.new_game(5, 5)
    t1 = Tribute()
    w1 = Weapon()
    p1 = Potion()
    game.board.put_tribute(2, 2, t1)
    game.board.put_item(2, 3, w1)
    game.board.put_item(3, 2, p1)
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos
    assert result == (2, 3)  # Closest item (Weapon) is at (2,3)


def test_tribute_vision_cells_ocupped_order_by_closeness_multiple_items(game):
    t1 = game.board.get_element(2, 2).get_tribute()
    game.board.put_item(3, 2, Potion())
    game.board.put_item(2, 1, Weapon())
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos
    assert result == (2, 1)  # Closest item (Weapon) is at (2, 1)


def test_fight_2_tributes_and_one_died():
    game = GameLogic()
    game.new_game(2, 2)
    district0 = District()
    district1 = District()
    t1 = Tribute()
    t2 = Tribute()
    district0.add_tribute(t1)
    district0.number_district = 0
    district1.number_district = 1
    district0.add_tribute(t1)
    district1.add_tribute(t2)
    district1.cant_tributes = 1
    game.districts.append(district0)
    game.districts.append(district1)
    t1.set_config_parameters(40, 20, 1, 0)
    t2.set_config_parameters(40, 20, 1, 1)
    game.board.put_tribute(0, 0, t1)
    game.board.put_tribute(0, 1, t2)

    game.fight(t1, t2)
    assert t2.life == 20
    game.fight(t2, t1)
    assert t1.life == 20
    assert t2 in game.districts[1].tributes
    game.fight(t1, t2)
    assert t2.is_dead()
    assert game.board.get_element(0, 1).get_state() == State.FREE
    assert not (t2 in game.districts[1].tributes)


def test_heuristic_tribute_move_towards_item():
    game = GameLogic()
    game.new_game(7, 7)
    tribute = Tribute()
    tribute.force = 2
    game.board.put_tribute(3, 3, tribute)

    weapon = Weapon()
    game.board.put_item(4, 3, weapon)

    game.heuristic_tribute_first_attempt(tribute)

    assert tribute.pos == (4, 3)


def test_heuristic_tribute_first_attempt_move_towards_tribute():
    game = GameLogic()
    game.new_game(7, 7)
    tribute1 = Tribute()
    tribute2 = Tribute()
    tribute1.set_config_parameters(50, 5, 5, 1)
    tribute2.set_config_parameters(50, 5, 5, 2)
    game.board.put_tribute(3, 3, tribute1)
    game.board.put_tribute(4, 3, tribute2)

    game.heuristic_tribute_first_attempt(tribute1)

    assert tribute1.pos == (3, 3)
    assert tribute2.life == 45


def test_heuristic_tribute_first_attempt_move_randomly():
    game = GameLogic()
    game.new_game(7, 7)
    tribute = Tribute()
    game.board.put_tribute(3, 3, tribute)

    game.heuristic_tribute_first_attempt(tribute)

    # El tributo debe haberse movido a una posición adyacente aleatoria
    assert tribute.pos != (3, 3)
    free_adjacents = game.board.random_choice(tribute)
    assert not (tribute.past_pos in free_adjacents)


def test_heuristic_tribute_first_attempt_neutral_potion():
    game = GameLogic()
    game.new_game(2, 2)

    # Configuración del tributo principal
    tribute = Tribute()
    tribute.set_config_parameters(50, 5, 25, 1)
    game.board.put_tribute(1, 1, tribute)

    # Configuración de tributo neutral (neutro)
    neutro = Tribute()
    game.board.put_tribute(0, 0, neutro)

    # Configuración de poción
    p = Potion()
    game.board.put_item(1, 0, p)
    game.heuristic_tribute_first_attempt(tribute)
    assert tribute.pos == p.pos


def test_heuristic_tribute_first_attempt_complex():
    game = GameLogic()
    game.new_game(5, 4)

    # Configuración del tributo principal
    tribute0 = Tribute()
    tribute0.set_config_parameters(50, 5, 25, 0)
    game.board.put_tribute(1, 1, tribute0)
    d0 = District()
    d0.number_district = 0
    d0.add_tribute(tribute0)
    game.districts.append(d0)
    # Configuración de tributo oponente (t1)
    t1 = Tribute()
    t1.set_config_parameters(10, 5, 1, 1)
    game.board.put_tribute(1, 3, t1)
    d1 = District()
    d1.number_district = 1
    d1.add_tribute(t1)
    game.districts.append(d1)
    # Configuración de tributo neutral (neutro)
    neutro = Tribute()
    game.board.put_tribute(4, 3, neutro)
    neutro.life = 20
    neutro.force = 10
    game.neutrals.append(neutro)

    # Configuración de arma y poción
    w = Weapon()
    p = Potion()
    game.board.put_item(2, 3, w)
    game.board.put_item(4, 2, p)

    game.heuristic_tribute_first_attempt(tribute0)
    game.heuristic_tribute_first_attempt(tribute0)
    assert tribute0.pos == w.pos
    assert tribute0.force == 10
    game.heuristic_tribute_first_attempt(tribute0)
    t1.attack_to(tribute0, game.board)
    game.heuristic_tribute_first_attempt(tribute0)
    assert tribute0.life == 45
    assert t1.is_dead()
    assert game.board.get_element(1, 3).get_state() == State.FREE
    game.heuristic_tribute_first_attempt(tribute0)
    game.heuristic_tribute_first_attempt(tribute0)
    assert tribute0.life == 50
    assert tribute0.pos == p.pos
    game.heuristic_tribute_first_attempt(tribute0)
    assert neutro in game.districts[0].tributes


def test_end_game():
    district1 = District()
    district2 = District()
    district1.set_config(50, 5, 3, 1, 2)
    district2.set_config(50, 5, 3, 2, 2)
    game = GameLogic()
    game.districts.append(district1)
    assert game.end_game() is district1  # end_game returns the only district alive
    game.districts.append(district2)
    assert game.end_game() is False
    game2 = GameLogic()
    with pytest.raises(ValueError):
        game2.end_game()
    # assert neutro.district == tribute.district


# Test for configuration_districts(...)

def test_config_districts_length_district():
    district = District()
    game_logic = GameLogic()
    game_logic.configuration_districts(district, 25, 5, 10, 1, 4)
    assert len(game_logic.districts) == 6


def test_config_districts_add_district():
    district = District()
    game_logic = GameLogic()
    game_logic.configuration_districts(district, 50, 7, 3, 2, 4)
    assert district in game_logic.districts


def test_config_districts_my_number_district():
    district = District()
    game_logic = GameLogic()
    game_logic.configuration_districts(district, 30, 10, 10, 2, 6)
    my_district = game_logic.districts[0]
    my_number_district = my_district.get_number_district()
    assert my_number_district == 2


def test_config_district_my_cant_tributes():
    district = District()
    game_logic = GameLogic()
    game_logic.configuration_districts(district, 50, 5, 5, 1, 5)
    my_district = game_logic.districts[0]
    my_cant_tributes = my_district.get_cant_tribute()
    assert my_cant_tributes == 5


def test_alliance_neutral_tribute():
    tribute = Tribute()
    district = District()
    district.set_config(50, 5, 5, 1, 2)
    old_number_of_tributes = district.get_cant_tribute()
    game = GameLogic()
    game.alliance_neutral(tribute, district)
    assert tribute.district is district.get_number_district()
    assert old_number_of_tributes + 1 == district.get_cant_tribute()
    assert district.tributes.__contains__(tribute)


def test_heuristic_of_game_simple_2_tribute_1_died(game2x2):
    game2x2.mode = GameMode.SIMULATION
    game2x2.heuristic_of_game()
    assert len(game2x2.districts[0].tributes) == 1
    assert len(game2x2.districts[1].tributes) == 0


def test_heuristic_of_game_simple_2_tribute_1_weapon_1_died(game2x2):
    w1 = Weapon()
    game2x2.board.put_item(1, 0, w1)
    game2x2.mode = GameMode.SIMULATION
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t2 = game2x2.board.get_element(0, 1).get_tribute()
    game2x2.heuristic_of_game()
    assert t2.is_dead()
    assert t1.force == 25
    assert t1.is_alive()

    assert len(game2x2.districts[0].tributes) == 1
    assert len(game2x2.districts[1].tributes) == 0


# fix potion problem, its not respect limit of tribute life
def test_heuristic_of_game_simple_2_tribute_1_potion_1_died(game2x2):
    p1 = Potion()
    game2x2.board.put_item(1, 0, p1)
    game2x2.mode = GameMode.SIMULATION
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t2 = game2x2.board.get_element(0, 1).get_tribute()
    game2x2.heuristic_of_game()
    assert t2.is_alive()
    assert t1.is_dead()
    assert len(game2x2.districts[0].tributes) == 0
    assert len(game2x2.districts[1].tributes) == 1


def test_heuristic_of_game_simple_2_tribute_1_neutral_success_1_died(game2x2):
    neutro = Tribute()
    neutro.life = 25
    neutro.force = 5

    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t1.life = 39

    t2 = game2x2.board.get_element(0, 1).get_tribute()
    t1.alliance = 25
    game2x2.board.put_tribute(1, 0, neutro)
    game2x2.mode = GameMode.SIMULATION
    game2x2.neutrals.append(neutro)
    game2x2.heuristic_of_game()
    assert t1.is_dead()
    assert neutro.life == -15
    assert t2.is_alive()
    assert len(game2x2.districts[0].tributes) == 0
    assert len(game2x2.districts[1].tributes) == 1


def test_heuristic_of_game_simple_2_tribute_1_neutral_fail_1_died():
    game = GameLogic()
    game.new_game(8, 8)
    game.mode = GameMode.SIMULATION
    district0 = District()
    district1 = District()
    t0 = Tribute()
    t1 = Tribute()
    district0.number_district = 0
    district1.number_district = 1
    game.districts.append(district0)
    game.districts.append(district1)
    t0.set_config_parameters(41, 20, 1, 0)
    t0.alliance = -25
    t1.set_config_parameters(40, 20, 1, 1)
    game.board.put_tribute(0, 0, t0)
    game.board.put_tribute(7, 7, t1)
    district0.add_tribute(t0)
    district1.add_tribute(t1)
    game.put_neutral(0, 1)
    game.heuristic_of_game()
    assert len(game.districts[0].tributes) == 0
    assert len(game.neutrals) == 0
    assert len(game.districts[1].tributes) == 1


# tests applies_effects(..) method

def test_applies_effects_potion():
    t1 = Tribute()
    t1.district = 0
    potion = Potion()
    game = GameLogic()
    game.new_game(2,2)
    game.put_tribute(0,0,t1)
    game.board.put_item(0,1,potion)
    t1.life = 45
    game.heuristic_tribute_first_attempt(t1)
    assert t1.life == 50
    t1.life = 30
    game.board.put_item(0,0,potion)
    game.heuristic_tribute_first_attempt(t1)
    assert t1.life == 40


def test_applies_effects_weapon():
    t1 = Tribute()
    t1.district = 0
    weapon = Weapon()
    game = GameLogic()
    game.new_game(2,2)
    game.put_tribute(0,0,t1)
    game.board.put_item(0,1,weapon)
    game.heuristic_tribute_first_attempt(t1)

    assert t1.force == 5 + WEAPON_EFFECT



# test for init_game(..)

def test_init_game_input_stats_own_district(monkeypatch):
    # Simula la entrada de datos por consola (donde configuro mi distrito)
    # Con vida: 50, fuerza: 7, alianza: 3, numero distrito: 0, cantidad tributos: 5
    monkeypatch.setattr('builtins.input', lambda x: '70' if 'Vida' in x 
                        else '7' if 'Fuerza' in x 
                        else '3' if 'Alianza' in x 
                        else '4' if 'Numero de distrito' in x 
                        else '4' if 'Cantidad de tributos' in x 
                        else '')
    
    game = GameLogic()
    game.init_simulation(8, 8)
    my_district = game.districts[0]

    for i in range(my_district.get_cant_tribute()):
        tribute_my_district = my_district.tributes[i]
        assert tribute_my_district.life == 70
        assert tribute_my_district.force == 7
        assert tribute_my_district.alliance == 3
        assert tribute_my_district.district == 4


def test_init_game_configure_random_districts(monkeypatch):
    # Simulo entrada de datos por consola para configurar mi distrito
    monkeypatch.setattr('builtins.input', lambda x: '50' if 'Vida' in x 
                        else '10' if 'Fuerza' in x 
                        else '5' if 'Alianza' in x 
                        else '2' if 'Numero de distrito' in x 
                        else '4' if 'Cantidad de tributos' in x 
                        else '')
    
    game = GameLogic()
    game.init_simulation(8, 8)
    my_num_district = game.districts[0].get_number_district() # recupero mi numero de distrito
    game.districts = game.districts[1:] # elimino mi distrito
    for i in range(5): # cinco distritos
        random_district = game.districts[i]
        for j in range(4):
            random_tribute = random_district.tributes[j]
            assert random_tribute.life == 50
            assert 5 <= random_tribute.force <= 10
            assert 3 <= random_tribute.alliance <= 10
            assert random_tribute.district != my_num_district


def test_init_game_distribute_tributes(monkeypatch):
    # Simulo entrada de datos por consola para configurar mi distrito
    monkeypatch.setattr('builtins.input', lambda x: '75' if 'Vida' in x 
                        else '8' if 'Fuerza' in x 
                        else '6' if 'Alianza' in x 
                        else '5' if 'Numero de distrito' in x 
                        else '6' if 'Cantidad de tributos' in x 
                        else '')
    
    game = GameLogic()
    game.init_simulation(8, 8)    
    tributes_count = 0
    
    # chequeo que se agregaron 26 tributos en el tablero
    for row in game.board.board:
        for cell in row:
            if cell.state == State.TRIBUTE:
                tributes_count += 1
    assert tributes_count == 26



def test_put_tribute():
    game = GameLogic()
    game.new_game(2, 2)
    t0 = Tribute()
    t0.set_config_parameters(50, 10, 4, 0)
    game.put_tribute(0, 0, t0)
    assert t0.pos == (0, 0)
    assert game.board.get_element(0, 0).get_tribute() == t0
    t1 = Tribute()
    t1.set_config_parameters(50, 10, 4, 1)
    game.put_tribute(1, 1, t1)
    assert t1.pos == (1, 1)
    assert game.board.get_element(1, 1).get_tribute() == t1
    assert len(game.districts) == 2
    s1 = Tribute()
    s1.set_config_parameters(50, 10, 4, 1)
    game.put_tribute(1, 0, s1)
    assert s1.pos == (1, 0)
    assert game.board.get_element(1, 0).get_tribute() == s1
    assert len(game.districts[1].tributes) == 2


def test_put_item():
    w = Weapon()
    game = GameLogic()
    game.new_game(2, 2)
    game.put_item(0, 0, w)
    assert game.board.get_element(0, 0).get_item().pos == (0, 0)
