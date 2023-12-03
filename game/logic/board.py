import random

from game.logic.cell import Cell, State
from game.logic.item import (
    Weapon,
    Spear,
    Sword,
    Bow,
    PotionPoison,
    PotionLife,
    PotionForce,
)
from game.logic.tribute import Tribute
from marshmallow import Schema, fields

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),
]


class Board:

    # Initializes an instance of the Board class with dimensions X and Y
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []
        for row in range(self.rows):
            curr_row = []
            for col in range(self.columns):
                cell = Cell()
                cell.pos = (row, col)
                curr_row.append(cell)
            self.board.append(curr_row)

    # Converts a string representing a board into an instance of the Board class.
    def from_string(board_str):
        from game.logic.district import District

        rows = board_str.split("\n")
        n_rows = len(rows)
        if n_rows < 1:
            raise ValueError(f"Invalid number of rows: {n_rows}")
        matrix = [row.split("|") for row in rows]
        n_cols = len(matrix[0])
        if n_cols < 1:
            raise ValueError(f"Invalid number of columns: {n_cols}")

        new_board = Board(n_rows, n_cols)
        districts, neutrals, order = [], [], [0, 1, 2, 3, 4, 5]
        for i in range(6):
            district = District()
            district.number_district = i
            districts.append(district)

        char_to_class = {  # Dicctionary that mapping chars to class
            "w": Weapon, "sp": Spear, "sw": Sword, "wo": Bow,
            "po": PotionPoison, "pl": PotionLife, "pf": PotionForce
        }
        for row in range(n_rows):
            for col in range(n_cols):
                char = matrix[row][col].strip()
                if char.startswith("n"):
                    tribute = Tribute()
                    tribute.pos = (row, col)
                    tribute.name = char
                    new_board.get_element(row, col).put_tribute(tribute)
                    neutrals.append(tribute)
                elif char.startswith(("t", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",)
                                     ):
                    # Check if it's a tribute character ('t') followed by a number
                    try:
                        tribute_number = int(char[1])
                        if 0 <= tribute_number <= 5:
                            tribute = Tribute()
                            tribute.name = char
                            tribute.set_config_parameters(50, 5, 3, tribute_number, 0)
                            districts[tribute_number].add_tribute(tribute)
                            new_board.put_tribute(row, col, tribute)
                        else:
                            raise ValueError(
                                f"Invalid tribute number: {tribute_number}"
                            )
                    except ValueError:
                        raise ValueError(f"Invalid tribute character: {char}")
                elif char == "  ":
                    pass
                elif char in char_to_class:
                    item_class = char_to_class[char]  # recovered class of item
                    item = item_class()  # create instance of class item
                    new_board.get_element(row, col).put_item(item)
                    item.pos = (row, col)
                elif char != "":
                    raise ValueError(f"Invalid character in board string: {char}")

        return [new_board, districts, neutrals, order]

    # Gets the cell at a specific position on the board.
    def get_element(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.board[row][column]
        else:
            raise ValueError(f"Invalid row or column index: ({row}, {column})")

    # Places a tribute at a specific position on the board.
    def put_tribute(self, row, column, tribute):
        if tribute.pos is None:
            tribute.past_pos = (row, column)
        else:
            tribute.past_pos = tribute.pos
        tribute.pos = (row, column)
        self.board[row][column].put_tribute(tribute)

    # Removes a tribute from the board.
    def remove_tribute(self, tribute):
        x = tribute.pos[0]
        y = tribute.pos[1]
        self.board[x][y].remove_tribute()

    # Places an item object at a specific position on the board.
    def put_item(self, row, column, item):
        item.pos = (row, column)
        self.board[row][column].put_item(item)

    # Removes an item object from the board.
    def remove_item(self, item):
        x = item.pos[0]
        y = item.pos[1]
        self.board[x][y].remove_item()

    # Distributes the tributes from a district to random positions on the board.
    def distribute_tributes(self, district):
        for i in range(district.cant_tributes):
            pos = self.random_pos()
            self.put_tribute(pos[0], pos[1], district.tributes[i])

    # Distribute items potions or items weapons on board.
    def distribute_items(self, item):
        for i in range(item.cant_items):
            pos = self.random_pos()
            self.put_item(pos[0], pos[1], item.items[i])

    # Creat and distribute one type of potion or weapon on board.
    def create_and_distribute_item(self, item, num_item):
        if item.is_potion():
            item.create_potion(num_item)
        else:
            item.create_weapon(num_item)
        self.distribute_items(item)

    # Distribute different types of potions on board.
    def distribute_potions(self):
        potion_list = [PotionLife, PotionForce, PotionPoison]
        for potion in potion_list:
            p = potion()
            self.create_and_distribute_item(p, 5)

    # Distribute different types of weapons on board.
    def distribute_weapons(self):
        weapon_list = [Sword, Spear, Bow]
        for weapon in weapon_list:
            w = weapon()
            self.create_and_distribute_item(w, 5)

    # Generates a random and valid position on the board.
    def random_pos(self):
        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            element = self.get_element(x, y)
            if element.state != State.TRIBUTE and element.state != State.ITEM:
                return x, y

    # Converts a row of cells on the board into a string representation.
    @staticmethod
    def _row_to_string(row):
        res = ""
        columns = len(row)
        for col in range(columns):
            cell = row[col]
            if cell.get_state() == State.FREE:
                res += "  "
            else:
                res += cell.__str__()  # Use the __str__ method of the cell
            if col < columns - 1:
                res += "|"
        return res

    # Represents the board as a text string.
    def __str__(self):
        res = ""
        for row_num in range(self.rows):
            res += Board._row_to_string(self.board[row_num])
            if row_num < self.rows - 1:
                res += "\n"
        return res

    # Returns the position of the tribute.
    @staticmethod
    def get_pos(tribute):
        return tribute.pos

    # Gets the cells adjacent to a specific position on the board.
    def get_adjacent_positions(self, row, column):
        adjacent_positions = []

        # Define the directions for adjacent cells, including the corners.

        for dr, dc in DIRECTIONS:
            new_row, new_column = row + dr, column + dc

            if 0 <= new_row < self.rows and 0 <= new_column < self.columns:
                adjacent_positions.append((new_row, new_column))

        return adjacent_positions

    # Check if a position on the board is valid and free.
    def valid_pos(self, pos):
        x = pos[0]
        y = pos[1]
        if x < 0 or x >= self.rows:
            return False
        if y < 0 or y >= self.columns:
            return False
        if self.get_element(x, y).get_state() == State.TRIBUTE:
            return False

        return True

    # Get the adjacent cells to a specific position on the board.
    def get_adjacents_cells(self, x, y):
        if not (0 <= x < self.rows) or not (0 <= y < self.columns):
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds")

        list_pos = self.get_adjacent_positions(x, y)
        adjacent_cells = []

        for pos in list_pos:
            x, y = pos
            if 0 <= x < self.rows and 0 <= y < self.columns:
                adjacent_cells.append(self.get_element(x, y))

        return adjacent_cells

    # Get the free adjacent cells to a specific position on the board.
    def get_free_adjacents_cells(self, x, y):
        if x < 0 or x >= self.rows or y < 0 or y >= self.columns:
            raise ValueError(f"Invalid position: x={x}, y={y} is out of range.")

        adjacents_cells = self.get_adjacents_cells(x, y)
        free_adjacents = []
        for cell in adjacents_cells:
            if cell.get_state() != State.TRIBUTE:
                free_adjacents.append(cell)
        return free_adjacents

    # Get the adjacent positions to a specific position on the board.
    def get_free_adjacents_positions(self, x, y):
        if x < 0 or x >= self.rows or y < 0 or y >= self.columns:
            raise ValueError(f"Invalid position: x={x}, y={y} is out of range.")

        free_positions = []
        for dr, dc in DIRECTIONS:
            new_row, new_column = x + dr, y + dc

            if 0 <= new_row < self.rows and 0 <= new_column < self.columns:
                element = self.get_element(new_row, new_column)
                if element.get_state() != State.TRIBUTE:
                    free_positions.append((new_row, new_column))

        return free_positions

    # Makes a random choice of a free adjacent position for a tribute without
    # considering the tribute's previous position.
    def random_choice(self, tribute):
        x = tribute.pos[0]
        y = tribute.pos[1]
        free_adjacents_pos = self.get_free_adjacents_positions(x, y)

        if tribute.past_pos in free_adjacents_pos:
            free_adjacents_pos.remove(tribute.past_pos)

        if not free_adjacents_pos:
            raise ValueError(
                f"No available free adjacent positions for Tribute {tribute}"
            )

        pos = random.choice(free_adjacents_pos)
        while self.board[pos[0]][pos[1]].get_state() == State.ITEM:
            pos = random.choice(free_adjacents_pos)

        return pos


class BoardSchema(Schema):
    rows = fields.Integer()
    columns = fields.Integer()
    board = fields.List(fields.List(fields.Str()))
