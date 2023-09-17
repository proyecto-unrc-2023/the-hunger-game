#GameLogic:
#  - start new game
#  - current mode
#  - get board
#  - set board from string
#  - put live cell
from enum import Enum

from game.logic.board import Board


class GameMode(Enum):
    NOT_STARTED = 1
    TRIBUTES_PLACEMENT = 2
    SIMULATION = 3

class GameLogic:

    def __init__(self):
        self.mode = GameMode.NOT_STARTED
        self.board = None
        self.columns = None
        self.rows = None

    def new_game(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = Board(rows, columns)
        self.mode = GameMode.TRIBUTES_PLACEMENT

