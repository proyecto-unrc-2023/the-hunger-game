# GameLogic:
#  - start new game
#  - current mode
#  - get board
#  - set board from string
#  - put live cell
from enum import Enum

from game.logic.board import Board
from game.logic.cell import State


class GameMode(Enum):
    NOT_STARTED = 1
    TRIBUTES_PLACEMENT = 2
    SIMULATION = 3


class GameLogic:

    def __init__(self):
        self.mode = GameMode.NOT_STARTED
        self.board = None
        self.districts = []
        self.neutrals = []

    def new_game(self, rows, columns):
        self.board = Board(rows, columns)
        self.mode = GameMode.TRIBUTES_PLACEMENT

    def tribute_vision_pos(self, tribute):
      visible_positions = []
      row = tribute.pos[0]
      column = tribute.pos[1]

      # Verificar las celdas adyacentes a 3 celdas a su alrededor
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1),
                     (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (-1, -2), (-1, 2), 
                     (-2, -2), (-2, 2), (1, -2), (1, 2), (2, -1), (2, 1), (2, -2), (2, 2),
                     (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -2), (-3, -1), (-3, 1), (-3, 2),
                     (-2, -3), (-2, 3), (-1, -3), (-1, 3), (-3, -3), (-3, 3), (1, -3), (1, 3),
                     (2, -3), (2, 3), (3, -2), (3, -1), (3, 2), (3, 1), (3, -3), (3, 3)]:
          new_row, new_column = row + dr, column + dc

          # Verificar si la posición es válida
          if 0 <= new_row < self.board.rows and 0 <= new_column < self.board.columns:
              visible_positions.append((new_row, new_column))

      return visible_positions
  
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

    def tribute_vision_cells_ocupped_order_by_closeness(self, tribute):      
        def calculate_distance(position):
            return ((position.pos[0] - tribute.get_pos()[0]) ** 2 + (position.pos[1] - tribute.get_pos()[1]) ** 2) ** 0.5
        
        vision_cells = self.tribute_vision_cells(tribute)  
       
        occupped_vision_cells = []
        for cell in vision_cells:
            if cell.get_state() != State.FREE:
                occupped_vision_cells.append(cell)

        occupped_vision_cells.sort(key=calculate_distance)

        if not  occupped_vision_cells:
            raise ValueError(f'No FREE positions')
        
        return occupped_vision_cells[0]

    def heuristic_tribute_first_attempt(self, tribute):
        vision_cells = self.tribute_vision_cells(tribute)
        for i in vision_cells:
            if vision_cells[i].get_state() == State.ITEM:
                pos_item = vision_cells[i].get_item().get_pos()
                self.board.move_closer_to(pos_item)
                break
            elif vision_cells[i].get_state() == State.TRIBUTE:
                pos_tribute = vision_cells[i].get_tribute().get_pos()
                self.board.move_closer_to(pos_tribute)
                break
            else:
                self.board.move_to_random(tribute)
                