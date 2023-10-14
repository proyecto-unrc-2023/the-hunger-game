from enum import Enum

from game.logic.board import Board
from game.logic.tribute import Tribute, LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT
from game.logic.cell import State
from game.logic.item import Item, Weapon, Potion
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
            tribute.name = letters[district_aux.cant_tributes-1] + str(district_aux.number_district)
        else:
            self.board.put_tribute(row, column, tribute)
            self.districts[tribute.district].add_tribute(tribute)
            tribute.name = letters[self.districts[tribute.district].cant_tributes -1] + str(self.districts[tribute.district].number_district)
                
    # Remove a Tribute of the board and of its district
    def remove_tribute(self, tribute):
        if tribute.district is None:
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
        neutral.name = 'n' + str(len(self.neutrals) -1)

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
            tribute.attack_to(tribute2, self.board)
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
            self.fight(neutral,neutral.enemy)
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
            if not (tribute.enemy is None):
                self.fight(tribute, tribute.enemy)
            else:
                if cell.get_state() == State.ITEM:
                    # If it's an item, go to retrieve it.
                    if (x,y) in self.board.get_adjacent_positions(Tx, Ty):
                        tribute.move_to(x, y, self.board)
                        item = cell.get_item()
                        self.applies_effects(item, tribute)
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
                            else:
                                tribute.enemy = cell.get_tribute()
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
        self.order_attack()
        if self.mode != GameMode.SIMULATION:
            raise ValueError(f'The state of the game is not SIMULATION')
        while self.end_game() == False:
            self.all_iteration()
            if not (self.neutrals is None):
                for neutral in self.neutrals:
                    self.neutral_heuristic(neutral)
            print("--------------------------------------------------------------")
            print(self.to_string())


    # This method create a new board, request by console stats of your district, 
    # configure five random districts and distributes tributes in board
    def init_simulation(self, rows, columns):
        self.new_game(rows, columns)        
        # Is necesary create an instance of district here and set by default every stat.
        district = District()
        life, force, alliance = LIFE_DEFAULT, FORCE_DEFAULT, ALLIANCE_DEFAULT 
        cant_tributes, number_district = 4, 0
        print(f"Board is {rows} x {columns}.")
        print("\nBy default, your number of district is", number_district)
        var_yes , points = 'y', 10
        # Beginning a big while    
        while var_yes == 'y': 
            print("\nYou have", points, "points available to distribute on:")
            print("1. Life")
            print("2. Force")
            print("3. Alliance")
            print("4. Tributes")
            try:
                choice = int(input("¿Where do you want to spend your points? Choose a number (1 - 4): "))
                # Choice 1 Life
                if choice == 1:
                    while True:
                        life_points = int(input("How many points do you want to spend on Life?: "))##no muestra por consola esto
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
                        tributes_points = int(input("How many points do you want to spend on Tributes? Each tribute costs 4 points: "))
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
                else:
                    print("Invalid option. Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number (1 - 4).")
            # If you spent all points then it asks if you want to reconfigure the district
            if points <= 0:
                print("\nYou have spent all your points.")
                print("The stats of your district are: \nLife:", life, "\nForce:", force, "\nAlliance:", alliance, "\nTributes:", cant_tributes)
                var_yes = input("Do you want to redistribute the points (y / n)?: ").strip().lower()
                while var_yes not in ('y', 'n'):
                    var_yes = input("Invalid input. Enter (y / n): ").strip().lower()
                
                # Choice y, then sets all stats like in beginning
                if var_yes == 'y':             
                    life, force, alliance = LIFE_DEFAULT , FORCE_DEFAULT, ALLIANCE_DEFAULT,  
                    # Remove tributes
                    for tribute in district.tributes:
                        district.remove_tribute(tribute)
                    points, cant_tributes = 10, 4

        if rows * columns < cant_tributes + 20:
            print("You must creat a board more bigger.")
            return                
        # Configure own district
        district.set_config(life, force, alliance, number_district, cant_tributes) 
        self.districts.append(district)
        # Configure others districts
        for i in range(6): 
            if i != number_district:
                district = District()
                district.cant_tributes = 4
                district.set_config_by_default(i)
                self.districts.append(district)
        # distribute items
        self.distribute_items_input(rows, columns, cant_tributes)
        # distribute districts
        for j in range(len(self.districts)):
            self.board.distribute_tributes(self.districts[j])     
        self.mode = GameMode.SIMULATION
        self.heuristic_of_game()
    
    # Distribute items on board according inputs.
    def distribute_items_input(self, rows, columns, cant_tributes):
        max_potions = (rows * columns) - cant_tributes - 20

        print("\nPut items on board.")
        while True:
            try:
                num_potions = int(input(f"How many potions do you want on board? Choice a number 0 between and {max_potions}: "))
                if 0 <= num_potions <= max_potions:
                    if num_potions == 0:
                        break
                    potion = Potion()
                    potion.create_item(num_potions)
                    self.board.distribute_items(potion)
                    break
                else:
                    print("Invalid input:", num_potions)
            except ValueError:
                print("Invalid input:", num_potions)
        
        max_weapons = max_potions - num_potions
        while True:
            try:
                num_weapons = int(input(f"How many weapons do you want on board? Choice a number between 0 and {max_weapons}: "))
                if 0 <= num_weapons <= max_weapons:
                    if num_weapons == 0:
                        break
                    weapon = Weapon()
                    weapon.create_item(num_weapons)
                    self.board.distribute_items(weapon)
                    break
                else:
                    print("Invalid input:", num_weapons)
            except ValueError:
                print("Invalid input:", num_weapons)

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

    def table_to_string(self, behave_table):
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
        print(self.order)
        
        self.order.append(temp)
        print(self.order)
        
        return self.order