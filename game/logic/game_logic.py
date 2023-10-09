from enum import Enum

from game.logic.board import Board
from game.logic.tribute import Tribute
from game.logic.cell import State
from game.logic.item import Weapon, Potion
from game.logic.district import District


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

    # Starts a new game with the specified number of rows and columns.
    def new_game(self, rows, columns):
        self.board = Board(rows, columns)
        self.mode = GameMode.TRIBUTES_PLACEMENT

    def from_string(self, str):
        result = Board.from_string(str)
        self.board = result[0]
        self.districts = result[1]
        
    # Method to add a tribute in a game
    # "tribute" is the tribute configured
    # Row and Column are the position of tribute
    def put_tribute(self, row, column, tribute):
        district = tribute.district
        district_aux = District()
        if len(self.districts) == district:
            district_aux.number_district = district
            district_aux.add_tribute(tribute)
            self.districts.append(district_aux)
            self.board.put_tribute(row, column, tribute)
        else:
            self.board.put_tribute(row, column, tribute)
            self.districts[tribute.district].add_tribute(tribute)

    # Remove a Tribute of the board and of its district
    def remove_tribute(self, tribute):
        if tribute.district == -99:
            self.neutrals.remove(tribute)
        else:
            self.districts[tribute.district].remove_tribute(tribute)

        self.board.remove_tribute(tribute)

    # Places a Item at a specific position on the board.
    def put_item(self, row, column, item):
        self.board.put_item(row, column, item)
        
    #Applies the effect of the item on the tribute and remove tribute of game.  
    def applies_effects(self, item, tribute):
        item.apply_effect(tribute)
        self.board.remove_item(item)
        
    # Places a Neutral at a specific position on the board and in Neutrals.
    def put_neutral(self, x, y):
        neutral = Tribute()
        self.board.put_tribute(x, y, neutral)
        self.neutrals.append(neutral)


    # Configure the own district with all stats that we need and configure five random districts 
    def configuration_districts(self, district, life, force, alliance, num_district, cant_tributes):

        district.set_config(life, force, alliance, num_district, cant_tributes)
        self.districts.append(district)
        my_num_district = district.get_number_district()
        list_district = [1, 2, 3, 4, 5, 6]
        list_district.remove(my_num_district)

        for i in range(5):
            district.set_config_random(list_district[i])
            self.districts.append(district)


    # Returns the positions visible to an tribute within an certain range.
    def tribute_vision_pos(self, tribute):
        visible_positions = []
        row = tribute.pos[0]
        column = tribute.pos[1]

        # Checks adjacent cells within a 3 radius.
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1),
                       (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (-2, -2), (-2, 2), (1, -2), (1, 2), (2, -1), (2, 1), (2, -2), (2, 2),
                       (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -2), (-3, -1), (-3, 1), (-3, 2),
                       (-2, -3), (-2, 3), (-1, -3), (-1, 3), (-3, -3), (-3, 3), (1, -3), (1, 3),
                       (2, -3), (2, 3), (3, -2), (3, -1), (3, 2), (3, 1), (3, -3), (3, 3)]:
            new_row, new_column = row + dr, column + dc

            if 0 <= new_row < self.board.rows and 0 <= new_column < self.board.columns:
                visible_positions.append((new_row, new_column))

        return visible_positions

    # Returns the list of visible cells for a tribute.
    def tribute_vision_cells(self, tribute):
        if not (0 <= tribute.pos[0] < self.board.rows) or not (0 <= tribute.pos[1] < self.board.columns):
            raise ValueError(f"Coordinates ({tribute.pos[0]}, {tribute.pos[1]}) are out of bounds")

        list_pos = self.tribute_vision_pos(tribute)
        tribute_visionCells = []

        for pos in list_pos:
            x, y = pos
            if 0 <= x < self.board.rows and 0 <= y < self.board.columns:
                tribute_visionCells.append(self.board.get_element(x, y))

        return tribute_visionCells

    # Returns the closest occupied cell to the tribute.    
    def tribute_vision_cells_ocupped_order_by_closeness(self, tribute):
        def calculate_distance(cell):
            distance = ((cell.get_pos()[0] - tribute.pos[0]) ** 2 + (cell.get_pos()[1] - tribute.pos[1]) ** 2) ** 0.5
            if cell.get_state() == State.ITEM:
                if cell.get_item() == Weapon():
                    distance -= 0.9
                else:
                    distance -= 0.8
            elif cell.get_state() == State.TRIBUTE:
                if cell.get_tribute().district == None:
                    distance -= 0.001

            return distance

        vision_cells = self.tribute_vision_cells(tribute)

        occupied_cells = [
            cell
            for cell in vision_cells
            if cell.get_state() == State.ITEM or (cell.get_state() == State.TRIBUTE and
                                                  cell.get_tribute().district != tribute.district)
            # && cell.get_state() != State.TRIBUTE para que sólo se fije en los ítems
            # && cell.get_state() != State.ITEM para que sólo se fije en los tributos
        ]

        occupied_cells.sort(key=calculate_distance)

        if not occupied_cells:
            return False

        return occupied_cells[0]

    # Simulates combat between two tributes, moving 'tribute' towards 'tribute2' 
    # and removing 'tribute2' if defeated.
    def fight(self, tribute, tribute2):
        x = tribute2.pos[0]
        y = tribute2.pos[1]
        pos = tribute.move_closer_to(x, y, self.board)
        if not (pos in self.board.get_adjacent_positions(tribute.pos[0], tribute.pos[1])):
            tribute.move_to(pos[0], pos[1], self.board)
        else:
            cell_with_tribute = self.board.get_element(x, y)
            t2 = cell_with_tribute.get_tribute()
            tribute.attack_to(t2, self.board)
            if tribute2.is_dead():
                self.remove_tribute(tribute2)

    # Method to use after the alliance is True
    # "Tribute" is the neutral tribute who accept the alliance
    def alliance_neutral(self, tribute, district):
        tribute.district = district.get_number_district()
        district.tributes.append(tribute)
        district.cant_tributes = district.cant_tributes + 1
    
    
    def neutral_heuristic(self, neutral):
        if neutral.district == -99:
            tribute = self.tribute_vision_cells_ocupped_order_by_closeness(neutral)
            self.fight(neutral,tribute)
        else:
            neutral.move_to_random(self.board)    
        
    
    
    # Implements a heuristic move for a tribute" in a game or simulation.
    def heuristic_tribute_first_attempt(self, tribute):
        # Find a nearby occupied cell ordered by closeness to the tribute.
        cell = self.tribute_vision_cells_ocupped_order_by_closeness(tribute)

        # If there are no occupied cells nearby, move the tribute to a random cell on the game board.
        if cell == False:
            tribute.move_to_random(self.board)
        else:
            # Get the position of the occupied cell in the vision.
            x = cell.pos[0]
            y = cell.pos[1]
            Tx = tribute.pos[0]
            Ty = tribute.pos[1]
            # Check the state of the cell (ITEM or TRIBUTE).
            if cell.get_state() == State.ITEM:
                # If it's an item, go to retrieve it.
                if cell.get_item().pos in self.board.get_adjacent_positions(Tx, Ty):
                    tribute.move_to(x, y, self.board)
                    item = cell.get_item()
                    item.apply_effect(tribute)
                    self.board.remove_item(item)
                else:
                    pos = tribute.move_closer_to(x, y, self.board)
                    tribute.move_to(pos[0], pos[1], self.board)

            elif cell.get_state() == State.TRIBUTE:
                # If it's a tribute,check if its a neutral or not
                if cell.get_tribute().district == None:
                    if cell.get_tribute().pos in self.board.get_adjacent_positions(Tx, Ty):
                        if tribute.alliance_to(cell.get_tribute()) == True:
                            district = self.districts[tribute.district]
                            self.alliance_neutral(cell.get_tribute(), district)
                            self.neutrals.remove(cell.get_tribute())
                        else:
                            cell.get_tribute().district = -99
                    else:
                        pos = tribute.move_closer_to(x, y, self.board)
                        tribute.move_to(pos[0], pos[1], self.board)
                else:
                    pos = cell.get_tribute().pos
                    # move to an adjacent position to it, and if already adjacent, attack.
                    if not (pos in self.board.get_adjacent_positions(tribute.pos[0], tribute.pos[1])):
                        pos = tribute.move_closer_to(x, y, self.board)
                        tribute.move_to(pos[0], pos[1], self.board)
                    else:
                        cell_with_tribute = self.board.get_element(x, y)
                        t2 = cell_with_tribute.get_tribute()
                        self.fight(tribute, t2)

    # Check which district won (literally return a district)
    # Return false if still in play
    def end_game(self):
        district_alive = District()
        cant_of_districts_alive = 0
        dead_districts = 0
        if len(self.districts) == 0:
            raise ValueError("There is not tributes in the game")
        else:
            for aux_district in self.districts:
                if aux_district.get_cant_tribute() == 0:
                    dead_districts = dead_districts + 1
                else:
                    cant_of_districts_alive = cant_of_districts_alive + 1
                    if cant_of_districts_alive >= 2:
                        return False
                    district_alive = aux_district
            if cant_of_districts_alive == 1:
                return district_alive

    def heuristic_of_game(self):
        if self.mode != GameMode.SIMULATION:
            raise ValueError(f'The state of the game is not SIMULATION')
        while self.end_game() == False:
            for district in self.districts:
                for tribute in district.tributes:
                    self.heuristic_tribute_first_attempt(tribute)
            if not (self.neutrals is None):
                for neutral in self.neutrals:
                    self.heuristic_tribute_first_attempt(neutral)


    # This method create a new board, request by console stats of your district, 
    # configure five random districts and distributes tributes in board
    def init_simulation(self, rows, columns):
        self.new_game(rows, columns)
        # Diccionary of parameters. When invoked init_simulation method, this 
        # request you for console: life, force, alliance, number_district and cant_tributes
        tributes_parameters = { 
            "life": int(input("Vida: ")),
            "force": int(input("Fuerza: ")),
            "alliance": int(input("Alianza: ")),
            "number_district": int(input("Numero de distrito: ")),
            "cant_tributes": int(input("Cantidad de tributos: ")),
        }

        district = District() 
        district.set_config(**tributes_parameters) # all inputs store in **tributes_parameters 
        self.districts.append(district)
        for i in range(6): 
            if i != tributes_parameters["number_district"]: # I dont want that my district configure again
                district = District()
                district.cant_tributes = 4
                district.set_config_random(i)
                self.districts.append(district)

        # distribute all tributes of districts in board       
        for j in range(len(self.districts)):
            self.board.distribute_tributes(self.districts[j]) 
	
        self.mode = GameMode.SIMULATION


    def one_iteration(self):
        for district in self.districts:
            for tribute in district.tributes:
                self.heuristic_tribute_first_attempt(tribute)
        if not (self.neutrals is None):
            for neutral in self.neutrals:
                self.heuristic_tribute_first_attempt(neutral)