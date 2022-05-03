from games.barca.piece import BarcaPiece


class Elephant(BarcaPiece):
    positionx = None
    positiony = None

    def __init__(self, name):
        super().__init__(name)

    def get_legal_moves(self, state):
        moves = []

    def initialize_positions(self, x, y):
        if self.positionx and self.positiony is None:
            self.positionx = x
            self.positiony = y
