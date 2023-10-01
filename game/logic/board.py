import random

from game.logic.cell import Cell, State
from game.logic.item import Weapon, Potion
from game.logic.tribute import Tribute


class Board:
    # Convierte un string que representa un tablero en una instancia de la clase Board.
    def from_string(board_str):
        rows = board_str.split('\n')
        n_rows = len(rows)
        if n_rows < 1:
            raise ValueError(f'Invalid number of rows: {n_rows}')
        matrix = [row.split('|') for row in rows]
        n_cols = len(matrix[0])
        if n_cols < 1:
            raise ValueError(f'Invalid number of columns: {n_cols}')

        new_board = Board(n_rows, n_cols)

        for row in range(n_rows):
            for col in range(n_cols):
                char = matrix[row][col].strip()
                if char == 't':
                    tribute = Tribute()
                    new_board.get_element(row, col).put_tribute(tribute)
                elif char == ' ':
                    pass
                elif char == 'w':
                    weapon = Weapon()
                    new_board.get_element(row, col).put_item(weapon)
                elif char == 'p':
                    potion = Potion()
                    new_board.get_element(row, col).put_item(potion)
                elif char != '':
                    raise ValueError(f'Invalid character in board string: {char}')

        return new_board

    # Crea una nueva instancia de la clase Board a partir de una matriz de tributos.
    @staticmethod
    def _from_string_matrix(rows, cols, matrix):
        new_board = Board(rows, cols)
        for row in range(rows):
            for col in range(cols):
                curr_tribute = matrix[row][col]
                new_board.put_tribute(row, col, Tribute.from_string(curr_tribute))
        return new_board

    # Inicializa una instancia de la clase Board con las dimensiones X e Y
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []
        for row in range(self.rows):
            curr_row = []
            for col in range(self.columns):
                cell = Cell()
                cell.pos = (row,col)
                curr_row.append(cell)
            self.board.append(curr_row)

    # Obtiene la celda en una posición específica del tablero.
    def get_element(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.board[row][column]
        else:
            raise ValueError(f'Invalid row or column index: ({row}, {column})')

    # Coloca un tributo en una posición específica del tablero.
    def put_tribute(self, row, column, tribute):
        tribute.pos = (row, column)
        self.board[row][column].put_tribute(tribute)

     # Elimina un tributo del tablero.
    def remove_tribute(self, tribute):
        x = tribute.pos[0]
        y = tribute.pos[1]
        self.board[x][y].remove_tribute()

    # Coloca un objeto item en una posición específica del tablero.
    def put_item(self, row, column, item):
        item.pos = (row, column)
        self.board[row][column].put_item(item)

    # Elimina un objeto item del tablero.
    def remove_item(self, item):
        x = item.pos[0]
        y = item.pos[1]
        self.board[x][y].remove_item()

    # Distribuye los tributos de un distrito en posiciones aleatorias del tablero.
    def distribute_tributes(self, district):
        for i in range(district.cant_tributes):
            pos = self.random_pos()
            self.put_tribute(pos[0], pos[1], district.tributes[i])

    # Genera una posición aleatoria y válida en el tablero.
    def random_pos(self):
        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            element = self.get_element(x, y)
            if element.state != State.TRIBUTE and element.state != State.ITEM:
                return x, y

    # Convierte una fila de celdas del tablero en una representación de cadena.
    @staticmethod
    def _row_to_string(row):
        res = ''
        columns = len(row)
        for col in range(columns):
            cell = row[col]
            if cell.get_state() == State.FREE:
                res += ' '
            else:
                res += cell.__str__()  # Use the __str__ method of the cell
            if col < columns - 1:
                res += '|'
        return res

    # Representa el tablero como una cadena de texto.
    def __str__(self):
        res = ''
        for row_num in range(self.rows):
            res += Board._row_to_string(self.board[row_num])
            if row_num < self.rows - 1:
                res += '\n'
        return res
    
    # Devuelve la posicion del tributo
    def get_pos(self, tribute):
        return tribute.pos
    
    # Obtiene las celdas adyacentes a una posición específica en el tablero.
    def get_adjacent_positions(self, row, column):
        adjacent_positions = []

        # Definir las direcciones para las celdas adyacentes, incluyendo las esquinas
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            new_row, new_column = row + dr, column + dc

            # Verificar si la posición es válida
            if 0 <= new_row < self.rows and 0 <= new_column < self.columns:
                adjacent_positions.append((new_row, new_column))

        return adjacent_positions

    # Verifica si una posición en el tablero es válida y está libre.
    def valid_pos(self, pos):
        x = pos[0]
        y = pos[1]
        if x < 0 or x >= self.rows:
            return False
        if y < 0 or y >= self.columns:
            return False
        if self.get_element(x, y).get_state() != State.FREE:
            return False

        return True

    # Obtiene las celdas adyacentes a una posición específica en el tablero.
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

    # Obtiene las celdas adyacentes libres a una posición específica en el tablero.
    def get_free_adjacents_cells(self, x, y):
        if x < 0 or x >= self.rows or y < 0 or y >= self.columns:
            raise ValueError(f"Invalid position: x={x}, y={y} is out of range.")

        adjacents_cells = self.get_adjacents_cells(x, y)
        free_adjacents = []
        for cell in adjacents_cells:
            if cell.get_state() == State.FREE:
                free_adjacents.append(cell)
        return free_adjacents

    # Obtiene las posiciones adyacentes a una posición específica en el tablero.
    def get_free_adjacents_positions(self, x, y):
        if x < 0 or x >= self.rows or y < 0 or y >= self.columns:
            raise ValueError(f"Invalid position: x={x}, y={y} is out of range.")

        free_positions = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_column = x + dr, y + dc

            # Verificar s|i la posición es válida
            if 0 <= new_row < self.rows and 0 <= new_column < self.columns:
                element = self.get_element(new_row, new_column)
                if element.get_state() == State.FREE:
                    free_positions.append((new_row, new_column))

        return free_positions
    
    # Realiza una elección aleatoria de una posición adyacente libre para un tributo.
    def random_choice(self, tribute):
        x = tribute.pos[0]
        y = tribute.pos[1]
        free_adjacents_pos = self.get_free_adjacents_positions(x, y)

        if not free_adjacents_pos:
            raise ValueError(f"No available free adjacent positions for Tribute {tribute}")

        random_position = random.choice(free_adjacents_pos)
        return random_position
    
    # Mueve un tributo a una posición adyacente libre seleccionada aleatoriamente.
    def move_to_random(self, tribute):
        self.remove_tribute(tribute)
        pos = self.random_choice(tribute)
        self.put_tribute(pos[0], pos[1], tribute)

    # Mueve un tributo a una posición específica en el tablero.
    def move_to(self, x, y, tribute):
        self.remove_tribute(tribute)
        if not (self.valid_pos(tribute.pos)):
            raise ValueError(f'Position no valid')
        if self.board[x][y].get_state() == State.TRIBUTE:
            raise ValueError(f'Position have a Tribute')
        valid_pos = self.get_free_adjacents_positions(tribute.pos[0], tribute.pos[1])
        if not ((x,y) in valid_pos):
              raise ValueError(f'Position is not Adjacent')
        
        self.put_tribute(x, y, tribute)

    # Mueve un tributo hacia una posición más cercana a las coordenadas (x, y).
    def move_closer_to(self, x, y, tribute):
        def calculate_distance(position):
            return ((position[0] - x) ** 2 + (position[1] - y) ** 2) ** 0.5

        possible_moves = self.get_free_adjacents_positions(tribute.pos[0], tribute.pos[1])
        possible_moves.sort(key=calculate_distance)
        if not  possible_moves:
            raise ValueError(f'No FREE positions')

        return possible_moves[0]
