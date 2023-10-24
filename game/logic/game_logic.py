from enum import Enum

from game.logic.board import Board, BoardSchema
from game.logic.tribute import Tribute, LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT, COWARDICE_DEFAULT, TributeSchema
from game.logic.cell import State
from game.logic.item import Weapon, Sword, Spear, Bow
from game.logic.district import District, TRIBUTES_DEFAULT, DistrictSchema
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
        district_aux = District()
        letters = 'tabcdefghijklm'
        if len(self.districts) == district:
            district_aux.number_district = district
            district_aux.add_tribute(tribute)
            self.districts.append(district_aux)
            self.board.put_tribute(row, column, tribute)
            tribute.name = letters[district_aux.cant_tributes - 1] + str(district_aux.number_district)
        else:
            self.board.put_tribute(row, column, tribute)
            self.districts[tribute.district].add_tribute(tribute)
            tribute.name = letters[self.districts[tribute.district].cant_tributes - 1] + str(
                self.districts[tribute.district].number_district)

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
        neutral = Tribute()
        self.board.put_tribute(x, y, neutral)
        self.neutrals.append(neutral)
        neutral.name = 'n' + str(len(self.neutrals) - 1)

    # Returns the closest occupied cell to the tribute.
    def tribute_vision_closeness(self, tribute):
        def calculate_distance(cell):
            distance = ((cell.get_pos()[0] - tribute.pos[0]) ** 2 + (cell.get_pos()[1] - tribute.pos[1]) ** 2) ** 0.5
            if cell.get_state() == State.ITEM:
                if cell.get_item() == Weapon():
                    distance -= 0.9
                else:
                    distance -= 0.8
            elif cell.get_state() == State.TRIBUTE:
                if cell.get_tribute().district is None:
                    distance -= 0.001

            return distance

        vision_cells = tribute.tribute_vision_cells(self.board)

        occupied_cells = [
            cell
            for cell in vision_cells
            if cell.get_state() == State.ITEM or
            (cell.get_state() == State.TRIBUTE and cell.get_tribute().district != tribute.district)
        ]

        if tribute.weapon:
            occupied_cells = [
                cell
                for cell in occupied_cells
                if cell.state == State.ITEM and cell.get_item().is_weapon() is False
                or cell.state == State.TRIBUTE
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
        if tribute.range == 3:
            tribute.attack_to(tribute2, self.board)
        elif tribute.range == 2:
            if ((x, y) in tribute.get_neighbors_2_distance(self.board) or
                    (x, y) in self.board.get_adjacent_positions(tribute.pos[0], tribute.pos[1])):
                tribute.attack_to(tribute2, self.board)
            else:
                pos = tribute.move_closer_to(x, y, self.board)
                tribute.move_to(pos[0], pos[1], self.board)
        else:
            if (x, y) in self.board.get_adjacent_positions(tribute.pos[0], tribute.pos[1]):
                tribute.attack_to(tribute2, self.board)
            else:
                pos = tribute.move_closer_to(x, y, self.board)
                tribute.move_to(pos[0], pos[1], self.board)

        if tribute2.is_dead():
            self.remove_tribute(tribute2)
            tribute.enemy = None

    # Method to use after the alliance is True
    # "Tribute" is the neutral tribute who accept the alliance
    def alliance_neutral(self, tribute, district):
        tribute.district = district.get_number_district()
        district.tributes.append(tribute)
        district.cant_tributes = district.cant_tributes + 1
        self.neutrals.remove(tribute)

    def neutral_heuristic(self, neutral):
        if not (neutral.enemy is None):
            self.fight(neutral, neutral.enemy)
        else:
            neutral.move_to_random(self.board)

    # Implements a heuristic move for a tribute in a game or simulation.
    def heuristic_tribute_first_attempt(self, tribute):
        # Find a nearby occupied cell ordered by closeness to the tribute.
        cell = self.tribute_vision_closeness(tribute)
        # If there are no occupied cells nearby, move the tribute to a random cell on the game board.
        if cell is False:
            tribute.move_to_random(self.board)
        else:
            # Get the position of the occupied cell in the vision.
            x = cell.pos[0]
            y = cell.pos[1]
            pos_x_t = tribute.pos[0]
            pos_y_t = tribute.pos[1]

            if not (tribute.enemy is None):
                self.fight(tribute, tribute.enemy)
            else:
                # Check the state of the cell (ITEM or TRIBUTE).
                if cell.get_state() == State.ITEM:
                    # If it's an item, go to retrieve it.
                    if (x, y) in self.board.get_adjacent_positions(pos_x_t, pos_y_t):
                        tribute.move_to(x, y, self.board)
                        item = cell.get_item()
                        self.applies_effects(item, tribute)
                        if tribute.is_dead():
                            self.remove_tribute(tribute)
                    else:
                        pos = tribute.move_closer_to(x, y, self.board)
                        tribute.move_to(pos[0], pos[1], self.board)
                elif cell.get_state() == State.TRIBUTE:
                    # If it's a tribute,check if it's a neutral or not
                    if cell.get_tribute().district is None:
                        if cell.get_tribute().pos in self.board.get_adjacent_positions(pos_x_t, pos_y_t):
                            if tribute.alliance_to(cell.get_tribute()) is True:
                                district = self.districts[tribute.district]
                                self.alliance_neutral(cell.get_tribute(), district)
                            else:
                                tribute.enemy = cell.get_tribute()
                        else:
                            pos = tribute.move_closer_to(x, y, self.board)
                            tribute.move_to(pos[0], pos[1], self.board)
                    else:
                        if tribute.cowardice > 0:
                            self.get_away(tribute, cell.get_tribute())
                        else:
                            # move to an adjacent position to it, and if already adjacent, attack.
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
        self.order_attack()
        if self.mode != GameMode.SIMULATION:
            raise ValueError(f'The state of the game is not SIMULATION')
        while self.end_game() is False:
            self.all_iteration()
            if not (self.neutrals is None):
                for neutral in self.neutrals:
                    self.neutral_heuristic(neutral)
            line = '-' * (self.board.columns * 3 - 3)
            print(line)
            print(self.to_string())

    # This method create a new board, request by console stats of your district,
    # configure five random districts, distributes items and tributes in board
    def init_simulation(self, rows, columns):
        self.new_game(rows, columns)
        # Is necessary create an instance of district here and set by default every stat.
        district = District()
        life, force, alliance, cowardice = LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT, COWARDICE_DEFAULT
        cant_tributes, number_district = TRIBUTES_DEFAULT, 0
        print(f"Board is {rows} x {columns}.")
        print("\nBy default, your number of district is", number_district)
        var_yes, points = 'y', 10
        while var_yes == 'y':
            print("\nYou have", points, "points available to distribute on:")
            print("1. Life")
            print("2. Force")
            print("3. Alliance")
            print("4. Tributes")
            print("5. Cowardice")
            try:
                choice = int(input("¿Where do you want to spend your points? Choose a number (1 - 5): "))
                # Choice 1 Life
                if choice == 1:
                    while True:
                        life_points = int(input("How many points do you want to spend on Life?: "))
                        if 1 <= life_points <= points:
                            life = life + (5 * life_points)
                            points -= life_points
                            print("Life increased to:", life)
                            break
                        else:
                            print("Invalid input. You have", points, "points.")
                # Choice 2 Force
                elif choice == 2:
                    while True:
                        force_points = int(input("How many points do you want to spend on Force?: "))
                        if 1 <= force_points <= points:
                            force = force + (2 * force_points)
                            points -= force_points
                            print("Force increased to:", force)
                            break
                        else:
                            print("Invalid input. You have", points, "points.")
                # Choice 3 Alliance
                elif choice == 3:
                    while True:
                        alli_points = int(input("How many points do you want to spend on Alliance?: "))
                        if alliance == 10:
                            print("Alliance is at 10. You can't spend more points on it.")
                            break
                        if 1 <= alli_points <= points and alli_points <= 7:
                            alliance += alli_points
                            points -= alli_points
                            print("Alliance increased by:", alliance)
                            break
                        elif 7 < alli_points <= 10:
                            print("The limit for spending points on alliance is 7.")
                            break
                        else:
                            print("Invalid input. You have", points, "points.")
                # Choice 4 Tributes
                elif choice == 4:
                    while True:
                        tributes_points = int(
                            input("How many points do you want to spend on Tributes? Each tribute costs 4 points: "))
                        if tributes_points in (4, 8):
                            required_points = tributes_points
                            num_tributes = tributes_points // 4
                            if points >= required_points:
                                cant_tributes += num_tributes
                                points -= required_points
                                print("The number of tributes increased to:", cant_tributes)
                                break
                            else:
                                print("You don't have enough points for this operation. You have", points, "points.")
                                break
                        else:
                            print("Invalid input. You should enter 4 or 8 points to spend on Tributes.")
                # Choice 5 Cowardice            
                elif choice == 5:
                    while True:
                        cowardice_points = int(input("How many points do you want to spend on Cowardice?: "))
                        if cowardice == 5:
                            print("Cowardice is at 5. You can't spend more points on it.")
                            break
                        if 1 <= cowardice_points <= points and cowardice_points <= 5:
                            cowardice += cowardice_points
                            points -= cowardice_points
                            print("Cowardice increased by:", cowardice)
                            break
                        elif 5 < cowardice_points <= 10:
                            print("The limit for spending points on cowardice is 5.")
                            break
                        else:
                            print("Invalid input. You have", points, "points.")
                else:
                    print("Invalid option. Please choose a number between 1 and 4.")

            except ValueError:
                print("Invalid input. Please enter a valid number (1 - 5).")
            # If you spent all points then it asks if you want to reconfigure the district
            if points <= 0:
                print("\nYou have spent all your points.")
                print("The stats of your district are: \nLife:", life, "\nForce:", force, "\nAlliance:", alliance,
                      "\nTributes:", cant_tributes, "\nCowardice:", cowardice)
                var_yes = input("Do you want to redistribute the points (y / n)?: ").strip().lower()
                while var_yes not in ('y', 'n'):
                    var_yes = input("Invalid input. Enter (y / n): ").strip().lower()

                # Choice y, then sets all stats like in beginning
                if var_yes == 'y':
                    life, force, alliance, cowardice = LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT, COWARDICE_DEFAULT
                    # Remove tributes
                    for tribute in district.tributes:
                        district.remove_tribute(tribute)
                    cant_tributes, points = TRIBUTES_DEFAULT, 10

        if rows * columns < cant_tributes + 20:
            print("You must creat a board more bigger.")
            return
        # Configure own district
        district.set_config(life, force, alliance, number_district, cant_tributes, cowardice)
        self.districts.append(district)
        # Configure others districts
        for i in range(6):
            if i != number_district:
                district = District()
                district.cant_tributes = TRIBUTES_DEFAULT
                district.set_config_by_default(i)
                self.districts.append(district)
        # Distribute potions and weapons
        self.board.distribute_potions()
        self.board.distribute_weapons()

        for j in range(len(self.districts)):
            self.board.distribute_tributes(self.districts[j])

        self.mode = GameMode.SIMULATION
        print(self.to_string())
        self.heuristic_of_game()

    def one_iteration(self):
        for district in self.districts:
            for tribute in district.tributes:
                self.heuristic_tribute_first_attempt(tribute)
        if not (self.neutrals is None):
            for neutral in self.neutrals:
                self.neutral_heuristic(neutral)

    # Distributes the tributes from a district to random positions on the board.
    def distribute_tributes(self):
        for j in range(len(self.districts)):
            for i in range(self.districts[j].cant_tributes):
                pos = self.board.random_pos()
                self.put_tribute(pos[0], pos[1], self.districts[j].tributes[i])

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
                self.heuristic_tribute_first_attempt(tribute)
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
        cant_tributes, cowardice = TRIBUTES_DEFAULT, COWARDICE_DEFAULT
        number_district = 0
        district.set_config(life, force, alliance, number_district, cant_tributes, cowardice)
        self.districts.append(district)
        # Configure districts by random
        for i in range(6):
            if i != number_district:
                district = District()
                district.cant_tributes = 4
                district.set_config_by_default(i)
                self.districts.append(district)

        # distribute all tributes of districts in board
        for j in range(len(self.districts)):
            self.board.distribute_tributes(self.districts[j])

    def get_away(self, tribute, enemy):
        pos = tribute.calculate_flee(enemy, self.board)
        if pos is not False:
            self.remove_tribute(tribute)
            self.districts[tribute.district].add_tribute(tribute)
            self.board.put_tribute(pos[0], pos[1], tribute)
            tribute.cowardice -= 0.5
        else:
            self.fight(tribute, enemy)


class GameLogicSchema(Schema):
    mode = fields.Str()
    board = fields.Nested(BoardSchema)
    districts = fields.Nested(DistrictSchema, many=True)
    neutrals = fields.Nested(TributeSchema, many=True)
