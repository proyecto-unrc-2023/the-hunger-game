import pytest

from game.logic.cell import State
from game.logic.game_logic import GameLogic
from game.logic.board import Board
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
    game.new_game(3,3)
    t1 =  Tribute()
    t2 =  Tribute()
    neutro =  Tribute()
    w = Weapon()
    p = Potion()
    t1.set_config_parameters(50,5,1,1)
    t2.set_config_parameters(50,5,1,2)
    game.board.put_tribute(1,1,t1)
    game.board.put_tribute(0,1,t2) #//arriba
    game.board.put_item(2,1,w)#ABAJO
    game.board.put_item(1,0,p)#izquierda
    game.board.put_tribute(1,2,neutro)#derecha
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (2,1)
    game.board.remove_item(w)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (1,0)
    game.board.remove_item(p)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (1,2)
    game.board.remove_tribute(neutro)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (0,1)
    
    
def test_get_tribute_closeness_with_same_district():
    game = GameLogic()
    game.new_game(7, 7)
    t1 = Tribute()
    t2 = Tribute()
    t1.set_config_parameters(50,5,1,1)
    t2.set_config_parameters(50,5,1,1)
    game.board.put_tribute(3, 3, t1)
    game.board.put_tribute(3, 4, t2)
    p = Potion()
    game.board.put_item(5,5,p)
    assert game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos == (3,4)

def test_tribute_vision_cells_ocupped_order_by_closeness_empty_board():
    game = GameLogic()
    game.new_game(5, 5)
    t1 = Tribute()
    game.board.put_tribute(2, 2, t1)
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1)
    assert result == False

def test_tribute_vision_cells_ocupped_order_by_closeness_tributes_only(game):
    t1 = game.board.get_element(2, 2).get_tribute()
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos
    assert result == (1, 1)  # Closest tribute is at (1, 1)

def test_tribute_vision_cells_ocupped_order_by_closeness_items_only():
    game = GameLogic()
    game.new_game(5, 5)
    t1 = Tribute()
    w1 = Weapon()
    p1 = Potion()
    game.board.put_tribute(2,2,t1)
    game.board.put_item(2,3,w1)
    game.board.put_item(3,2,p1)
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos
    assert result == (2,3)  # Closest item (Weapon) is at (2,3)

def test_tribute_vision_cells_ocupped_order_by_closeness_multiple_items(game):
    t1 = game.board.get_element(2, 2).get_tribute()
    game.board.put_item(3, 2, Potion())
    game.board.put_item(2, 1, Weapon())
    result = game.tribute_vision_cells_ocupped_order_by_closeness(t1).pos
    assert result == (2, 1)  # Closest item (Weapon) is at (2, 1)
    
def test_fight_2_tributes_and_one_died():
    game = GameLogic()
    game.new_game(2,2)
    t1 = Tribute()
    t2 = Tribute()
    t1.set_config_parameters(40,25,1,1)
    t2.set_config_parameters(40,25,1,2)
    game.board.put_tribute(0,0,t1)
    game.board.put_tribute(0,1,t2)
    game.fight(t1,t2)
    assert t2.life == 15
    game.fight(t2,t1)
    assert t1.life == 15
    game.fight(t1, t2)
    assert t2.is_dead()
    assert game.board.get_element(0,1).get_state() == State.FREE
    
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
    tribute1.set_config_parameters(50,5,5,1)
    tribute2.set_config_parameters(50,5,5,2)
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
    tribute = Tribute()
    tribute.set_config_parameters(50, 5, 25, 1)
    game.board.put_tribute(1, 1, tribute)

    # Configuración de tributo oponente (t1)
    t1 = Tribute()
    t1.set_config_parameters(10, 5, 1, 2)
    game.board.put_tribute(1, 3, t1)  
    
    # Configuración de tributo neutral (neutro)
    neutro = Tribute()
    game.board.put_tribute(4, 3, neutro)  

    # Configuración de arma y poción
    w = Weapon()
    p = Potion()
    game.board.put_item(2, 3, w)
    game.board.put_item(4, 2, p)

    game.heuristic_tribute_first_attempt(tribute)
    game.heuristic_tribute_first_attempt(tribute)
    assert tribute.pos == w.pos
    assert tribute.force == 6
    game.board.remove_item(w)
    game.heuristic_tribute_first_attempt(tribute)
    t1.attack_to(tribute, game.board)
    game.heuristic_tribute_first_attempt(tribute)
    assert tribute.life == 45
    assert t1.is_dead()
    assert game.board.get_element(1,3).get_state() == State.FREE
    game.heuristic_tribute_first_attempt(tribute)
    game.heuristic_tribute_first_attempt(tribute)
    assert tribute.life == 50
    assert tribute.pos == p.pos
    game.heuristic_tribute_first_attempt(tribute)
    #assert neutro.district == tribute.district


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