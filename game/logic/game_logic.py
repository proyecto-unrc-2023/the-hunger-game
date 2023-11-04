from enum import Enum

from game.logic.board import Board
from game.logic.tribute import (
    LIFE_DEFAULT,
    FORCE_DEFAULT,
    ALLIANCE_DEFAULT,
    COWARDICE_DEFAULT,
)
from game.logic.cell import State
from game.logic.item import Weapon
from game.logic.district import District, TRIBUTES_DEFAULT, DISTRICT_DEFAULT
from marshmallow import Schema, fields


class GameMode(Enum):
    NOT_STARTED = 1
    TRIBUTES_PLACEMENT = 2
    SIMULATION = 3


class GameLogic:
    # Initializes the GameLogic instance.
    def __init__(self):
        self.mode = GameMode.NOT_STARTED
        self.board = None
        self.districts = []
        self.neutrals = []
        self.order = []
        self.winner = None

    # Starts a new game with the specified number of rows and columns.
    def new_game(self, rows, columns):
        self.board = Board(rows, columns)
        self.mode = GameMode.TRIBUTES_PLACEMENT

    def from_string(self, str):
        result = Board.from_string(str)
        self.board = result[0]
        self.districts = result[1]
        self.neutrals = result[2]
        self.order = result[3]

    def to_string(self):
        return self.board.__str__()

    # Method to add a tribute in a game
    # "tribute" is the tribute configured
    # Row and Column are the position of tribute
    def put_tribute(self, row, column, tribute):
        district = tribute.district
        if len(self.districts) == district:
            district_aux = District()
            district_aux.number_district = district
            district_aux.add_tribute(tribute)
            district_aux.asign_name_tribute(tribute)
            self.districts.append(district_aux)
            self.board.put_tribute(row, column, tribute)

        else:
            self.board.put_tribute(row, column, tribute)
            self.districts[tribute.district].add_tribute(tribute)
            self.districts[tribute.district].asign_name_tribute(tribute)

    # Remove a Tribute of the board and of its district
    def remove_tribute(self, tribute):
        if tribute.district is None:
            self.neutrals.remove(tribute)
        else:
            self.districts[tribute.district].remove_tribute(tribute)

        self.board.remove_tribute(tribute)

    # Places an Item at a specific position on the board.
    def put_item(self, row, column, item):
        self.board.put_item(row, column, item)

    # Applies the effect of the item on the tribute and remove tribute of game.
    def applies_effects(self, item, tribute):
        item.apply_effect(tribute)
        self.board.remove_item(item)

    # Places a Neutral at a specific position on the board and in Neutrals.
    def put_neutral(self, x, y):
        from game.logic.tribute import Tribute

        neutral = Tribute()
        self.board.put_tribute(x, y, neutral)
        self.neutrals.append(neutral)
        neutral.name = "n" + str(len(self.neutrals) - 1)

    # Configure five random districts. Stats force and alliance are random, others are by default.
    def configure_random_districts(self):
        for i in range(6):
            if i != DISTRICT_DEFAULT:
                district = District()
                district.set_config_random(i)
                self.districts.append(district)

    # Returns the closest occupied cell to the tribute.
    def tribute_vision_closeness(self, tribute):
        vision_cells = tribute.tribute_vision_cells(self.board)
        occupied_cells = self.calculate_occupied_cells(vision_cells, tribute)
        occupied_cells.sort(key=lambda cell: self.calculate_distance(cell, tribute))
        if not occupied_cells:
            return False

        return occupied_cells[0]

    def calculate_distance(self, cell, tribute):
        distance = (
                           (cell.get_pos()[0] - tribute.pos[0]) ** 2
                           + (cell.get_pos()[1] - tribute.pos[1]) ** 2
                   ) ** 0.5
        if cell.get_state() == State.ITEM:
            if cell.get_item() == Weapon():
                distance -= 0.9
            else:
                distance -= 0.8
        elif cell.get_state() == State.TRIBUTE:
            if cell.get_tribute().district is None:
                distance -= 0.001

        return distance

    @staticmethod
    def calculate_occupied_cells(vision_cells, tribute):
        occupied_cells = [
            cell
            for cell in vision_cells
            if cell.get_state() == State.ITEM or (
                    cell.get_state() == State.TRIBUTE and
                    cell.get_tribute().district != tribute.district
            )
        ]

        if tribute.weapon:
            occupied_cells = [
                cell
                for cell in occupied_cells
                if cell.state == State.ITEM and cell.get_item().is_weapon() is False
                or cell.state == State.TRIBUTE
            ]

        return occupied_cells

    # Simulates combat between two tributes, moving 'tribute' towards 'tribute2'
    # and removing 'tribute2' if defeated.
    def fight(self, tribute, tribute2):
        x = tribute2.pos[0]
        y = tribute2.pos[1]
        if tribute.range == 3:
            tribute.attack_to(tribute2, self.board)
        elif tribute.range == 2:
            self.attack_in_range_2(tribute, tribute2, x, y)
        else:
            self.attack_in_range_1(tribute, tribute2, x, y)
        if tribute2.is_dead():
            self.remove_tribute(tribute2)
            tribute.enemy = None

    def attack_in_range_2(self, tribute, tribute2, x, y):
        if (x, y) in tribute.get_neighbors_2_distance(self.board) or (
            x,
            y,
        ) in self.board.get_adjacent_positions(tribute.pos[0], tribute.pos[1]):
            tribute.attack_to(tribute2, self.board)
        else:
            pos = tribute.move_closer_to(x, y, self.board)
            tribute.move_to(pos[0], pos[1], self.board)

    def attack_in_range_1(self, tribute, tribute2, x, y):
        if (x, y) in self.board.get_adjacent_positions(
                tribute.pos[0], tribute.pos[1]
        ):
            tribute.attack_to(tribute2, self.board)
        else:
            pos = (x, y)
            tribute.step_to(self.board, pos)
            
    # Method to use after the alliance is True
    # "Tribute" is the neutral tribute who accept the alliance
    def alliance_neutral(self, tribute, district):
        tribute.district = district.get_number_district()
        district.asign_name_tribute(tribute)
        district.tributes.append(tribute)
        district.cant_tributes = district.cant_tributes + 1
        self.neutrals.remove(tribute)

    def neutral_heuristic(self, neutral):
        if not (neutral.enemy is None) and neutral.enemy.is_alive():
            if neutral.district == neutral.enemy.district:
                neutral.move_to_random(self.board)
            else:
                self.fight(neutral, neutral.enemy)
        else:
            neutral.enemy = None
            neutral.move_to_random(self.board)

    # Method that enables a tribute to move towards or pick up an item when the
    # item is in an adjacent location
    def try_take_item(self, tribute, pos):
        (tribute_x, tribute_y) = tribute.pos
        (x, y) = pos
        if (x, y) in self.board.get_adjacent_positions(tribute_x, tribute_y):
            tribute.move_to(x, y, self.board)
            item = self.get_cell((x, y)).get_item()
            self.applies_effects(item, tribute)
            if tribute.is_dead():
                self.remove_tribute(tribute)
        else:
            tribute.step_to(self.board, pos)

    # A method that allows the tribute to attack the enemy if they are in range
    # or move towards them if not
    def try_attack(self, tribute, pos):
        (x, y) = (pos[0], pos[1])
        cell = self.board.get_element(x, y)
        t2 = cell.get_tribute()
        self.fight(tribute, t2)

    # Method that allows the tribute to attempt aliance with an neutral
    def try_alliance(self, tribute, cell):
        (tribute_x, tribute_y) = (tribute.pos[0], tribute.pos[1])
        if cell.get_tribute().pos in self.board.get_adjacent_positions(
                tribute_x, tribute_y
        ):
            if tribute.alliance_to(cell.get_tribute()) is True:
                district = self.districts[tribute.district]
                self.alliance_neutral(cell.get_tribute(), district)
            else:
                tribute.enemy = cell.get_tribute()
        else:
            tribute.step_to(self.board, cell.pos)

    # Implements a heuristic move for a tribute in a game or simulation.
    def heuristic_tribute(self, tribute):
        cell = self.tribute_vision_closeness(tribute)
        if cell is False:
            tribute.move_to_random(self.board)
        else:
            if not (tribute.enemy is None) and tribute.enemy.is_alive() and tribute.district != tribute.enemy.district:
                self.fight(tribute, tribute.enemy)
            else:
                tribute.enemy = None
                if cell.get_state() == State.ITEM:
                    self.try_take_item(tribute, cell.pos)
                elif cell.get_state() == State.TRIBUTE:
                    if cell.get_tribute().district is None:
                        self.try_alliance(tribute, cell)
                    else:
                        if tribute.cowardice > 0:
                            self.get_away(tribute, cell.get_tribute())
                        else:
                            self.try_attack(tribute, cell.pos)


    def heuristic_of_game(self):
        self.order_attack()
        if self.mode != GameMode.SIMULATION:
            raise ValueError(f"The state of the game is not SIMULATION")
        while not self.game_ended():
            self.all_iteration()
            if self.neutrals:
                for neutral in self.neutrals:
                    self.neutral_heuristic(neutral)
            line = "-" * (self.board.columns * 3 - 3)
            print(line)
            print(self.to_string())

    def one_iteration(self):
        for district in self.districts:
            for tribute in district.tributes:
                self.heuristic_tribute(tribute)
        if self.neutrals:
            for neutral in self.neutrals:
                self.neutral_heuristic(neutral)
        return self

    # Distribute tributes from a district to random positions on the board.
    # This method is only for test.
    def distribute_tributes(self):
        for j in range(len(self.districts)):
            for i in range(self.districts[j].cant_tributes):
                pos = self.board.random_pos()
                self.put_tribute(pos[0], pos[1], self.districts[j].tributes[i])

    # Distribute neutral tributes on board given a number of neutral tributes.
    def distribute_neutral_tributes(self, number):
        for i in range(number):
            pos = self.board.random_pos()
            self.put_neutral(pos[0], pos[1])

    @staticmethod
    def table_to_string(behave_table):
        rows = []
        for row in behave_table:
            row_str = "|".join(row)
            rows.append(row_str)
        return "\n".join(rows)

    def order_attack(self):
        for i in range(len(self.districts)):
            self.order.append(i)

        return self.order

    def all_iteration(self):
        for i in range(len(self.districts)):
            num_district = self.order[i]
            for tribute in self.districts[num_district].tributes:
                self.heuristic_tribute(tribute)
        temp = self.order.pop(0)
        self.order.append(temp)

    # This method is a copy of init_simulation, avoiding the part of
    # configuring the district, assigns all default values and does NOT
    # start the simulation
    # IS ONLY FOR TEST, DON'T USE IN OTHER CONTEXT
    def prepare_the_game(self, rows, columns):
        self.new_game(rows, columns)
        district = District()
        life, force, alliance = LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT
        cant_tributes, cowardice, number_district = (
            TRIBUTES_DEFAULT,
            COWARDICE_DEFAULT,
            DISTRICT_DEFAULT,
        )

        district.set_config(
            life, force, alliance, number_district, cant_tributes, cowardice
        )
        self.districts.append(district)
        self.configure_random_districts()
        self.distribute_items()
        self.distribute_district_tributes()
        self.distribute_neutral_tributes(10)

    def get_away(self, tribute, enemy):
        pos = tribute.calculate_flee(enemy, self.board)
        if pos is not False:
            self.remove_tribute(tribute)
            self.districts[tribute.district].add_tribute(tribute)
            self.board.put_tribute(pos[0], pos[1], tribute)
            tribute.cowardice -= 0.5
        else:
            self.fight(tribute, enemy)

    # Method to get a tribute only by name
    def get_tribute_by_name(self, name_tribute):
        district = name_tribute[1]
        number_district = int(district)
        length = self.districts[number_district].tributes.__len__()
        for i in range(length):
            if self.districts[number_district].tributes[i].name == name_tribute:
                return self.districts[number_district].tributes[i]

    # Method to get a neutral only by name
    def get_neutral_by_name(self, name_neutral):
        number = int(name_neutral[1])
        return self.neutrals[number]

    # Method to get a list of tributes.
    # Param district is a number of district
    def get_list_tributes(self, district):
        return self.districts[district].tributes

    # Method to get the item in the position (x,y)
    def get_item_pos(self, x, y):
        return self.board.get_element(x, y).get_item()

    # Method to access to tribute position
    def get_tribute_pos(self, name_tribute):
        tribute = self.get_tribute_by_name(name_tribute)
        return tribute.pos

    # Method to return the cell in pos
    def get_cell(self, pos):
        return self.board.get_element(pos[0], pos[1])

    # Method to check if game is ended
    def game_ended(self):
        if len(self.districts) == 0:
            raise ValueError("There is not tributes in the game")
        districts_alive = 0
        for i in range(self.districts.__len__()):
            if self.districts[i].cant_tributes >= 1:
                districts_alive += 1
        if districts_alive == 1:
            return True
        else:
            return False

    # Method for returning the number of winner district. Return none if no winner district yet
    # else number of district winner.
    def winner_district(self):
        if self.game_ended():
            for i in range(len(self.districts)):
                if self.districts[i].cant_tributes >= 1:
                    self.winner = self.districts[i].number_district
        return self.winner

    # Set stats of own district. Front use this method
    def set_parameters(
            self, number_district, life, force, alliance, cant_tributes, cowardice
    ):
        my_district = District()
        my_district.set_config(
            life, force, alliance, number_district, cant_tributes, cowardice
        )
        self.districts.insert(0, my_district)

    # Distribute items on board. Front use this method
    def distribute_items(self):
        self.board.distribute_potions()
        self.board.distribute_weapons()

    # Distribute all districts of tributes on board. Fron use this method
    def distribute_district_tributes(self):
        for i in range(len(self.districts)):
            self.board.distribute_tributes(self.districts[i])

    # Execute one iteration for each tribute of districts. Finalize when exists just one live distric.
    # Front use this method.
    def one_iteration_front(self):
        while not self.game_ended():
            for district in self.districts:
                for tribute in district.tributes:
                    self.heuristic_tribute(tribute)
            if self.neutrals:
                for neutral in self.neutrals:
                    self.neutral_heuristic(neutral)
            return self


class GameLogicSchema(Schema):
    from game.logic.district import DistrictSchema
    from game.logic.board import BoardSchema
    from game.logic.tribute import TributeSchema

    mode = fields.Str()
    board = fields.Nested(BoardSchema)
    districts = fields.Nested(DistrictSchema, many=True)
    neutrals = fields.Nested(TributeSchema, many=True)
    winner = fields.Integer(allow_none=True)  # Permitir que el atributo winner sea None
