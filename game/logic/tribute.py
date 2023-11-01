import random

from marshmallow import Schema, fields

MAX_LIFE_DEFAULT = 50
LIFE_DEFAULT = 50

FORCE_DEFAULT = 5

ALLIANCE_DEFAULT = 3
RANGE_DEFAULT = 1
COWARDICE_DEFAULT = 0
MAX_COWARDICE = 5
POSSIBLE_POSITIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1),
                      (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (-1, -2), (-1, 2),
                      (-2, -2), (-2, 2), (1, -2), (1, 2), (2, -1), (2, 1), (2, -2), (2, 2),
                      (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -2), (-3, -1), (-3, 1), (-3, 2),
                      (-2, -3), (-2, 3), (-1, -3), (-1, 3), (-3, -3), (-3, 3), (1, -3), (1, 3),
                      (2, -3), (2, 3), (3, -2), (3, -1), (3, 2), (3, 1), (3, -3), (3, 3)]


class Tribute:

    def __init__(self):
        self.name = 't '
        self.life = LIFE_DEFAULT
        self.force = FORCE_DEFAULT
        self.alliance = ALLIANCE_DEFAULT
        self.cowardice = COWARDICE_DEFAULT
        self.district = None
        self.pos = None
        self.past_pos = None
        self.weapon = False
        self.max_life = MAX_LIFE_DEFAULT
        self.enemy = None
        self.range = RANGE_DEFAULT

    @staticmethod
    def from_string(tribute_str):
        if tribute_str.startswith(('t', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm')):
            t = Tribute()
            t.name = tribute_str
            return t
        else:
            raise ValueError(f'Invalid tribute string: {tribute_str}')

    def is_alive(self):
        if self.life > 0:
            return True

    def is_dead(self):
        if self.life <= 0:
            return True

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        if not isinstance(other, Tribute):
            return False
        if self.name != other.name:
            return False
        if self.alliance != other.alliance:
            return False
        if self.force != other.force:
            return False
        if self.district != other.district:
            return False
        if self.life != other.life:
            return False

        return True

    def attack_to(self, tribute, board):
        if tribute.district != self.district:
            tribute.life -= self.force
        else:
            raise ValueError(f"Not possible attack, same district")

    def set_config_parameters(self, life, force, alliance, district, cowardice):
        self.life = life
        self.force = force
        self.alliance = alliance
        self.district = district
        self.cowardice = cowardice

    # First proposal of the alliance system
    # The neutral tribute alliance is fictitious, it does not take said value
    # after the decision.
    # True if the alliance is successful, false otherwise
    def alliance_to(self, tribute):
        if tribute.district is not None:
            raise ValueError("The tribute is not Neutral")
        if self.generates_alliance_value(self.alliance, random.randint(1, 10)) is True:
            return True
        else:
            tribute.enemy = self
            return False

    @staticmethod
    def generates_alliance_value(tribute_alliance, neutral_tribute):
        neutral_tribute_alliance = neutral_tribute
        alliance = tribute_alliance + neutral_tribute_alliance
        alliance = alliance / 25
        if alliance >= 0.5:
            return True
        else:
            return False

    # Moves a tribute to a randomly selected free adjacent position.
    def move_to_random(self, board):
        board.remove_tribute(self)
        pos = board.random_choice(self)
        board.put_tribute(pos[0], pos[1], self)

    def move_to_diff_pos_random(self, board, x, y):
        board.remove_tribute(self)
        pos = board.random_choice(self)
        while pos == (x, y):
            pos = board.random_choice(self)
        board.put_tribute(pos[0], pos[1], self)

    # Moves a tribute to a specific position on the board.
    def move_to(self, x, y, board):
        from game.logic.cell import State

        board.remove_tribute(self)
        if not (board.valid_pos(self.pos)):
            raise ValueError(f'Position no valid')
        if board.board[x][y].get_state() == State.TRIBUTE:
            raise ValueError(f'Position have a Tribute')
        adjacent_pos = board.get_free_adjacents_positions(self.pos[0], self.pos[1])
        if not ((x, y) in adjacent_pos):
            raise ValueError(f'Position ({x}, {y}) is not free Adjacent')

        board.put_tribute(x, y, self)

    # Returns the closest position to coordinates (x, y) that a tribute can move to.
    def move_closer_to(self, x, y, board):
        def calculate_distance(position):
            return ((position[0] - x) ** 2 + (position[1] - y) ** 2) ** 0.5

        possible_moves = board.get_free_adjacents_positions(self.pos[0], self.pos[1])
        possible_moves.sort(key=calculate_distance)
        if not possible_moves:
            raise ValueError(f'No FREE positions, ignorar este error hasta que pueda solucionarlo')

        return possible_moves[0]

    # Method to determine the cells that are free within a two-cell distance
    def get_neighbors_2_distance_free(self, board):
        from game.logic.cell import State
        neighbors = []

        possible_neighbors = self.get_neighbors_2_distance(board)

        for pos in possible_neighbors:
            if (0 <= pos[0] < board.rows) and (0 <= pos[1] < board.columns):
                if board.get_element(pos[0], pos[1]).get_state() == State.FREE:
                    neighbors.append((pos[0], pos[1]))

        return neighbors

    # Method to determine the neighbors within a two-cell distance of a tribute
    def get_neighbors_2_distance(self, board):
        (x, y) = self.pos
        neighbors = []

        possible_neighbors = [
            (x - 2, y - 2), (x - 2, y - 1), (x - 2, y), (x - 2, y + 1), (x - 2, y + 2),
            (x - 1, y - 2), (x, y - 2), (x + 1, y - 2), (x + 2, y - 2),
            (x + 2, y - 1), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2),
            (x - 1, y + 2), (x, y + 2), (x + 1, y + 2)
        ]

        for i, j in possible_neighbors:
            if (0 <= i < board.rows) and (0 <= j < board.columns):
                neighbors.append((i, j))

        return neighbors

    # Method to know if a tribute has to escape down or up, left or right
    def flee_direction(self, enemy):
        (tribute_x, tribute_y) = self.pos
        (enemy_x, enemy_y) = enemy.pos
        if enemy_x > tribute_x:
            x_escape = [tribute_x - 2, tribute_x - 1, tribute_x]
        else:
            x_escape = [tribute_x + 2, tribute_x + 1, tribute_x]
        if enemy_y > tribute_y:
            y_escape = [tribute_y - 2, tribute_y - 1, tribute_y]
        else:
            y_escape = [tribute_y + 2, tribute_y + 1, tribute_y]
        return x_escape, y_escape

    # Method for calculate the best escape for a tribute with cowardice
    def calculate_flee(self, enemy, board):
        neighbors = self.get_neighbors_2_distance_free(board)
        if neighbors is None:
            return False
        (x_escape, y_escape) = self.flee_direction(enemy)
        for x in x_escape:
            for y in y_escape:
                if (x, y) in neighbors:
                    if (x, y) != (self.pos):
                        return (x, y)

        return neighbors[0]

    # Returns the positions visible to an tribute within an certain range.
    def tribute_vision_pos(self, board):
        visible_positions = []
        row = self.pos[0]
        column = self.pos[1]
        # Checks adjacent cells within a 3 radius.
        for dr, dc in POSSIBLE_POSITIONS:
            new_row, new_column = row + dr, column + dc
            if 0 <= new_row < board.rows and 0 <= new_column < board.columns:
                visible_positions.append((new_row, new_column))
        return visible_positions

    # Returns the list of visible cells for a tribute.
    def tribute_vision_cells(self, board):
        if not (0 <= self.pos[0] < board.rows) or not (0 <= self.pos[1] < board.columns):
            raise ValueError(f"Coordinates ({self.pos[0]}, {self.pos[1]}) are out of bounds")

        list_pos = self.tribute_vision_pos(board)
        tribute_vision_cells = []

        for pos in list_pos:
            x, y = pos
            if 0 <= x < board.rows and 0 <= y < board.columns:
                tribute_vision_cells.append(board.get_element(x, y))

        return tribute_vision_cells

    # Method to move the tribute one cell closer to the position
    def step_to(self, board, pos):
        (x, y) = pos
        pos = self.move_closer_to(x, y, board)
        self.move_to(pos[0], pos[1], board)


class TributeSchema(Schema):
    name = fields.Str()
    life = fields.Integer()
    force = fields.Integer()
    alliance = fields.Integer()
    cowardice = fields.Integer()
    district = fields.Integer()
    pos = fields.Tuple((fields.Integer(), fields.Integer()), required=True)
