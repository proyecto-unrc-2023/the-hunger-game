import random


class Tribute:

    def __init__(self):
        self.life = None
        self.force = None
        self.alliance = None
        self.district = None
        self.pos = None

    @staticmethod
    def from_string(tribute_str):
        if tribute_str == Tribute().__str__():
            return Tribute()  # from_string takes "t" and returns Tribute()
        else:
            raise ValueError(f'Invalid tribute string: {tribute_str}')

    def is_alive(self):
        if self.life > 0:
            return True

    def is_dead(self):
        if self.life == 0:
            return True

    def __str__(self):
        if self.district is None:
            return 't'
        else:
            return 't' + str(self.district.get_number_district())

    def __eq__(self, other):
        return isinstance(other, Tribute)

    def attack_to(self, tribute, board):
        listadj = board.get_adjacent_positions(self.pos[0], self.pos[1])
        if (tribute.pos[0], tribute.pos[1]) in listadj:
            tribute.life -= self.force
        else:
            raise ValueError(f"Not possible attack")

        if self.district is None:
            return 't'
        else:
            return 't' + str(self.district.get_number_district())

    def set_config_parameters(self, life, force, alliance, district):
        self.life = life
        self.force = force
        self.alliance = alliance
        self.district = district

    def move_to(self, position):
        # I check if current_pos exists
        if not self.pos:
            raise ValueError("Current position is not set for LiveTribute.")

        # I get all available moves
        available_moves = self.movements_available

        # I check if the movement is valid
        if position in available_moves:
            self.pos = position
        else:
            raise ValueError("Position is not an available movement for LiveTribute")

    # First proposal of the alliance system
    # The neutral tribute alliance is fictitious, it does not take said value
    # after the decision.
    def alliance_to(self, tribute):
        if tribute.district is not None:
            raise ValueError("The tribute is not Neutral")
        if self.generates_alliance_value(self.alliance, random.randint(1, 10)) is True:
            # Here, we need copy the District properties to neutral Tribute
            return True
        else:
            # Should be attack each other (IdK if that action be here or in other class )
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
