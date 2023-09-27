#Board:
#  - rows
#  - columns
#  - to string
#  - create from string
#  - put live tribute
from game.logic.tribute import DeadTribute, LiveTribute, Tribute
from game.logic.object import Item, Weapon, Potion
import random

class Board:

    def from_string(board_str):
        rows = board_str.split('\n')
        n_rows = len(rows)
        if n_rows < 1:
            raise ValueError(f'Invalid number of rows: {n_rows}')
        matrix = [row.split('|') for row in rows]
        n_cols = len(matrix[0])
        if n_cols < 1:
            raise ValueError(f'Invalid number of columns: {n_cols}')

        new_board = Board(n_rows, n_cols)  # Crear un nuevo tablero

        for row in range(n_rows):
            for col in range(n_cols):
                char = matrix[row][col].strip()
                if char == 't':
                    new_board.put_tribute(row, col, LiveTribute())
                elif char == ' ':
                    new_board.put_tribute(row, col, DeadTribute())
                elif char == 'w':
                    new_board.put_item(row, col, Weapon())
                elif char == 'p':
                    new_board.put_item(row, col, Potion())
                elif char != '':
                    raise ValueError(f'Invalid character in board string: {char}')

        return new_board

    @staticmethod
    def _from_string_matrix(rows, cols, matrix):
        new_board = Board(rows, cols)
        for row in range(rows):
            for col in range(cols):
                curr_tribute = matrix[row][col]
                new_board.put_tribute(row, col, Tribute.from_string(curr_tribute))
        return new_board

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []
        for row in range(self.rows):
            curr_row = []
            for col in range(self.columns):
                curr_row.append(DeadTribute())
            self.board.append(curr_row)

    def get_element(self, row, column):
        return self.board[row][column]

    def put_live_tribute(self, row, column):
        if self.get_element(row, column).__eq__(LiveTribute()):
            raise ValueError

        tribute = Tribute()
        tribute.pos = (row,column)
        self.board[row][column] = tribute

    def put_dead_tribute(self, row, column):
        element = self.get_element(row, column)
        if isinstance(element, DeadTribute):
            raise ValueError

        self.board[row][column] = DeadTribute()

    def put_tribute(self, row, column, tribute):
        element = self.get_element(row, column)
        if isinstance(element, LiveTribute) or isinstance(element, Item):
            raise ValueError

        tribute.pos = (row,column)
        self.board[row][column] = tribute

    def remove_tribute(self, tribute):
        x = tribute.pos[0]
        y = tribute.pos[1]
        element = self.get_element(x, y)
        if element.__eq__(Item) or element.__eq__(DeadTribute):
            raise ValueError

        self.put_dead_tribute(x, y)

    def put_item(self, row, column, item):
        if row > self.rows or column > self.columns:
            raise ValueError(f'Row or Columns out of range')
        element = self.get_element(row, column)
        if element.__eq__(LiveTribute):
            raise ValueError

        self.board[row][column] = item
        
    def remove_item(self, Item):
        element = self.get_element(Item.pos[0],Item.pos[1])
        if isinstance(element, LiveTribute) or isinstance(element, DeadTribute):
            raise ValueError(f'Trying to remove a Tribute')
        
        self.put_dead_tribute(Item.pos[0],Item.pos[1])

    def distribute_tributes(self, district):
        for i in range(district.cant_tributes):
            self.put_tribute(self.random_pos(), district.tributes[i])


    def random_pos(self):
        while True:
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.columns-1)
            element = self.get_element(x, y)
            if not isinstance(element, (LiveTribute, Item)):
                return (x,y)


    @staticmethod
    def _row_to_string(row):
        res = ''
        columns = len(row)
        for col in range(columns):
            res += row[col].__str__()
            if col < columns - 1:
                res += '|'
        return res

    def __str__(self):
        res = ''
        for row_num in range(self.rows):
            res += Board._row_to_string(self.board[row_num])
            if row_num < self.rows - 1:
                res += '\n'
        return res

    def get_pos(self, tribute):
        return tribute.pos
