import pytest

from game.logic.cell import State
from game.logic.district import District
from game.logic.game_logic import GameLogic, GameMode
from game.logic.item import Potion, Weapon
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


def test_from_string_and_to_string():
    game = GameLogic()
    board_str = 't3|t2\n' \
                't4|t1\n' \
                'n4|n1'
    game.from_string(board_str)
    assert board_str == game.to_string()
    assert len(game.districts[1].tributes) == 1
    assert len(game.districts[2].tributes) == 1
    assert len(game.districts[3].tributes) == 1
    assert len(game.districts[4].tributes) == 1
    assert len(game.neutrals) == 2
    t1 = game.board.get_element(1, 1).get_tribute()
    game.remove_tribute(t1)
    assert len(game.districts[1].tributes) == 0
    
def test_put_neutral(game2x2):
    game2x2.put_neutral(1, 0)
    game2x2.put_neutral(1, 1)
    neutral = game2x2.board.get_element(1, 0).get_tribute()
    neutral1 = game2x2.board.get_element(1, 1).get_tribute()
    assert neutral.name == 'n0'
    assert neutral1.name == 'n1'
    assert neutral.life == 50
    assert neutral.force == 5
    assert neutral.pos == (1, 0)
    assert neutral.district is None
    assert len(game2x2.neutrals) == 2


def test_remove_tribute2():
    game = GameLogic()
    game.new_game(3,3)
    t0 = Tribute()
    t1 = Tribute()
    t2 = Tribute()
    t0.set_config_parameters(50,4,3,0)
    t1.set_config_parameters(51,4,3,0)
    t2.set_config_parameters(52,4,3,0)
    game.put_tribute(0,0,t0)
    game.put_tribute(0,1,t1)
    game.put_tribute(1,0,t2)
    game.remove_tribute(t1)

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


def test_get_adjacents_cells_complex():
    game = GameLogic()
    game.new_game(8, 8)
    x, y = 0, 0
    game.board.put_tribute(1, 0, Tribute())
    game.board.put_tribute(0, 1, Tribute())
    game.board.put_tribute(1, 1, Tribute())
    adjacent_cells = game.board.get_adjacents_cells(x, y)
    assert len(adjacent_cells) == 3
    assert game.board.get_element(0, 1) in adjacent_cells
    assert game.board.get_element(1, 0) in adjacent_cells
    assert game.board.get_element(1, 1) in adjacent_cells
    # Modifica el cuarto assert
    assert len([cell for cell in adjacent_cells if cell.get_pos() == (7, 7)]) == 0
    with pytest.raises(ValueError):
        game.board.get_adjacents_cells(-1, 1)


def test_get_tribute_closenes_complex():
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
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1,0).pos == (2, 1)
    game.board.remove_item(w)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1,0).pos == (1, 0)
    game.board.remove_item(p)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1,0).pos == (1, 2)
    game.board.remove_tribute(neutro)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1,0).pos == (0, 1)
    game.board.remove_tribute(t2)
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1,0)
    assert result == False
    t2.district = 1
    game.board.put_tribute(2,2, t2)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1,0) == False
    w1 = Weapon()
    p1 = Potion()
    game.board.put_item(2, 1, w1)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1,0).pos == (2,1)
    

#####################

def test_fight_2_tributes_and_one_died():
    game = GameLogic()
    game.new_game(2, 2)
    district0 = District()
    district1 = District()
    t1 = Tribute()
    t2 = Tribute()
    t1.set_config_parameters(40, 20, 1, 0)
    t2.set_config_parameters(40, 20, 1, 1)
    game.put_tribute(0, 0, t1)
    game.put_tribute(0, 1, t2)
    game.fight(t1, t2)
    assert t2.life == 20
    game.fight(t2, t1)
    assert t1.life == 20
    assert t2 in game.districts[1].tributes
    game.fight(t1, t2)
    assert t2.is_dead()
    assert game.board.get_element(0, 1).get_state() == State.FREE
    assert not (t2 in game.districts[1].tributes)


def test_heuristic_tribute_complex():
    game = GameLogic()
    game.new_game(7, 7)
    tribute = Tribute()
    tribute.set_config_parameters(50,5,3,0)
    game.put_tribute(3, 3, tribute)
    weapon = Weapon()
    game.board.put_item(4, 3, weapon)
    #use Weapon
    game.heuristic_tribute_first_attempt(tribute)
    assert tribute.pos == (4, 3)
    assert tribute.force == 10
    tribute1 = Tribute()
    tribute1.set_config_parameters(50, 5, 5, 1)
    game.put_tribute(4,2,tribute1)
    #fight
    game.heuristic_tribute_first_attempt(tribute)
    game.heuristic_tribute_first_attempt(tribute1)
    assert tribute.life == 45
    assert tribute1.life == 40
    game.remove_tribute(tribute1)
    #random move
    game.heuristic_tribute_first_attempt(tribute)
    assert tribute.pos != (4,3)
    #neutral exito
    game.put_neutral(4,3)
    tribute.alliance = 25
    game.heuristic_tribute_first_attempt(tribute)
    assert len(game.districts[0].tributes) == 2
    #neutral fail
    neutral = game.board.get_element(4,3).get_tribute()
    game.remove_tribute(neutral)
    game.put_neutral(4,3)
    tribute.alliance = -25
    game.heuristic_tribute_first_attempt(tribute)
    assert len(game.districts[0].tributes) == 1
    assert tribute.enemy is not None

def test_heuristic_tribute_first_attempt_complex2():
    game = GameLogic()
    game.new_game(5, 4)

    # Config Tribute0
    tribute0 = Tribute()
    tribute0.set_config_parameters(50, 5, 25, 0)
    game.board.put_tribute(1, 1, tribute0)
    d0 = District()
    d0.number_district = 0
    d0.add_tribute(tribute0)
    game.districts.append(d0)
    # Config Tribute enemy t1
    t1 = Tribute()
    t1.set_config_parameters(10, 5, 1, 1)
    game.board.put_tribute(1, 3, t1)
    d1 = District()
    d1.number_district = 1
    d1.add_tribute(t1)
    game.districts.append(d1)
    # Config of Neutral
    neutro = Tribute()
    game.board.put_tribute(4, 3, neutro)
    neutro.life = 20
    neutro.force = 10
    game.neutrals.append(neutro)

    # Config of Weapon and Potion
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


def test_alliance_neutral_tribute():
    district = District()
    district.set_config(50, 6, 4, 0, 1)
    game = GameLogic()
    game.new_game(2,2)
    game.put_neutral(0, 0)
    neutral = game.neutrals[0]
    game.alliance_neutral(neutral, district)
    assert neutral.district is district.get_number_district()
    assert 1 + 1 == district.get_cant_tribute()
    assert district.tributes.__contains__(neutral)


def test_heuristic_of_game_simple_2_tribute_1_died(game2x2):
    game2x2.mode = GameMode.SIMULATION
    game2x2.heuristic_of_game()
    assert len(game2x2.districts[0].tributes) == 1
    assert len(game2x2.districts[1].tributes) == 0

def test_heuristic_of_game_simple_2_tribute_1_weapon_1_died(game2x2):
    w1 = Weapon()
    game2x2.put_item(1, 0, w1)
    game2x2.mode = GameMode.SIMULATION
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t2 = game2x2.board.get_element(0, 1).get_tribute()
    game2x2.heuristic_of_game()
    assert t2.is_dead()
    assert t1.force == 25
    assert t1.is_alive()
    assert len(game2x2.districts[0].tributes) == 1
    assert len(game2x2.districts[1].tributes) == 0


def test_heuristic_of_game_simple_2_tribute_1_potion_1_died(game2x2):
    p1 = Potion()
    game2x2.put_item(1, 0, p1)
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
    t1 = game2x2.board.get_element(0, 0).get_tribute()
    t2 = game2x2.board.get_element(0, 1).get_tribute()
    t1.alliance = 25
    game2x2.board.put_tribute(1, 0, neutro)
    game2x2.mode = GameMode.SIMULATION
    game2x2.neutrals.append(neutro)
    game2x2.heuristic_of_game()
    assert t1.is_alive()
    assert neutro.life == 25
    assert t2.is_dead()
    assert len(game2x2.districts[0].tributes) == 2
    assert len(game2x2.districts[1].tributes) == 0


def test_heuristic_of_game_simple_2_tribute_1_neutral_fail_1_died():
    game = GameLogic()
    game.new_game(8, 8)
    game.mode = GameMode.SIMULATION
    t0 = Tribute()
    t1 = Tribute()
    t0.set_config_parameters(50, 10, -25, 0)
    t1.set_config_parameters(40, 20, 1, 1)
    game.put_tribute(0, 0, t0)
    game.put_tribute(7, 7, t1)
    game.put_neutral(0, 1)
    game.heuristic_of_game()
    assert len(game.neutrals) == 0
    assert len(game.districts[0].tributes) == 0
    assert len(game.districts[1].tributes) == 1


def test_applies_effects_complex():
    t1 = Tribute()
    t1.district = 0
    potion = Potion()
    game = GameLogic()
    game.new_game(2,2)
    game.put_tribute(0,0,t1)
    game.put_item(0,1,potion)
    t1.life = 45
    game.heuristic_tribute_first_attempt(t1)
    assert t1.life == 50
    game.put_item(0,0,potion)
    game.heuristic_tribute_first_attempt(t1)
    assert t1.life == 50
    game.put_item(0,1,Weapon())
    game.heuristic_tribute_first_attempt(t1)
    assert t1.force == 10


def test_init_simulation_inputs_one(monkeypatch):
    game = GameLogic()
    user_inputs = iter(['1', '5', '4', '4', '2', '1', 'n', '10', '10']) # first is number_district, then choice, points,..., yes or no 
    
    def mock_input(prompt):
        return next(user_inputs)
    
    monkeypatch.setattr('builtins.input', mock_input)
    game.init_simulation(15, 15)
    my_district = game.districts[0]

    for i in range(len(my_district.tributes)):
        tribute_my_district = my_district.tributes[i]
        assert tribute_my_district.district == 0
        assert tribute_my_district.alliance == 3
 

def test_init_simulation_inputs_two(monkeypatch):
    game = GameLogic()
    user_inputs = iter(['4', '8', '1', '1', '3', '1', 'n', '8', '8']) # first is number_district, then choice, points,..., yes or no 
    
    def mock_input(prompt):
        return next(user_inputs)
    
    monkeypatch.setattr('builtins.input', mock_input)
    game.init_simulation(15, 15)
    my_district = game.districts[0]

    for i in range(len(my_district.tributes)):
        tribute_my_district = my_district.tributes[i]
        assert tribute_my_district.district == 0
        assert tribute_my_district.alliance == 4
     

def test_put_tribute():
    game = GameLogic()
    game.new_game(2, 2)
    t0 = Tribute()
    t0.set_config_parameters(50, 10, 4, 0)
    game.put_tribute(0, 0, t0)
    assert t0.name == 't0'
    assert t0.pos == (0, 0)
    assert game.board.get_element(0, 0).get_tribute() == t0
    t1 = Tribute()
    t1.set_config_parameters(50, 10, 4, 1)
    game.put_tribute(1, 1, t1)
    assert t1.name  == 't1'
    assert t1.pos == (1, 1)
    assert game.board.get_element(1, 1).get_tribute() == t1
    assert len(game.districts) == 2
    s1 = Tribute()
    s1.set_config_parameters(50, 10, 4, 1)
    game.put_tribute(1, 0, s1)
    assert s1.name == 'a1'
    assert s1.pos == (1, 0)
    assert game.board.get_element(1, 0).get_tribute() == s1
    assert len(game.districts[1].tributes) == 2

def test_put_item():
    w = Weapon()
    game = GameLogic()
    game.new_game(2, 2)
    game.put_item(0, 0, w)
    assert game.board.get_element(0, 0).get_item().pos == (0, 0)

def test_neutral_heuristic():
    game = GameLogic()
    game.new_game(3,3)
    t0 = Tribute()
    t1 = Tribute()
    t0.set_config_parameters(60,5,-25,0)
    t1.set_config_parameters(60,5,-25,1)
    game.put_tribute(0,0,t0)
    game.put_tribute(0,2,t1)
    game.put_neutral(0,1)
    game.heuristic_tribute_first_attempt(t0)
    game.heuristic_tribute_first_attempt(t1)
    neutral = game.board.get_element(0,1).get_tribute()
    game.neutral_heuristic(neutral)
    assert t1.life == 55
    assert t0.life == 60
    game.remove_tribute(t0)
    game.remove_tribute(t1)
    neutral.enemy = None
    game.neutral_heuristic(neutral)
    assert neutral.pos != (0,1)

def test_order_attack():
    game = GameLogic()
    game.new_game(2,2)
    #config t0
    t0 = Tribute()
    t0.set_config_parameters(50,5,3,0)
    game.put_tribute(0,0,t0)
    #config t1
    t1 = Tribute()
    t1.set_config_parameters(50,5,3,1)
    game.put_tribute(0,1,t1)
    #config t2
    t2 = Tribute()
    t2.set_config_parameters(50,5,3,2)
    game.put_tribute(1,1,t2)
    game.order_attack()
    assert game.order == [0,1,2]
    game.all_iteration()
    assert game.order == [1,2,0]
    game.all_iteration()
    assert game.order == [2,0,1]
    game.all_iteration()
    
def test_get_away():
    game = GameLogic()
    game.new_game(5,5)
    #config tributes
    t0 = Tribute()
    t0.set_config_parameters(50,5,3,0)
    game.put_tribute(0, 0, t0)
    t1 = Tribute()
    t1.set_config_parameters(50,5,3,1)
    game.put_tribute(0, 1, t1)
    #first iteration, can escape down
    game.heuristic_tribute_first_attempt(t0)
    assert t1.life == 45
    game.get_away(t1,t0)
    assert t1.pos == (2,3)
    #second, can escape left
    game.remove_tribute(t0)
    game.remove_tribute(t1) 
    game.put_tribute(4, 3, t1)
    game.put_tribute(4, 4, t0)
    game.get_away(t1,t0)
    assert t1.pos == (4,1)
    #third, can escape up left
    game.remove_tribute(t0)
    game.remove_tribute(t1) 
    game.put_tribute(4, 3, t0)
    game.put_tribute(4, 4, t1)
    game.get_away(t1,t0)
    assert t1.pos == (2,2)
    
def test_heuristic_get_away():
    game = GameLogic()
    game.new_game(6,6)
    #config tributes
    t0 = Tribute()
    t0.set_config_parameters(50,5,3,0)
    game.put_tribute(0, 0, t0)
    t1 = Tribute()
    t1.cowardice = 1
    t1.set_config_parameters(50,5,3,1)
    game.put_tribute(0, 1, t1)
    #first iteration, can escape down
    game.one_iteration()
    assert t1.pos == (2,3)
    assert t1.life == 45
    assert t1.cowardice == 0.5
    game.one_iteration()
    assert t1.pos == (4,5)
    assert t0.pos == (1,1)
    assert t1.cowardice == 0
    