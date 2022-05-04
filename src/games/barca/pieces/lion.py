from games.barca.piece import BarcaPiece


class Lion(BarcaPiece):
    position_x = None
    position_y = None

    def __init__(self, name):
        super().__init__(name)

    def initialize_positions(self, x, y):
        if self.positionx and self.positiony is None:
            self.positionx = x
            self.positiony = y

    def possible_moves(self):
        ur = [(self.positiony - i, self.positionx + i) for i in range(1, 10) if
              0 <= self.positionx < 10 and 0 <= self.positiony < 10]
        ul = [(self.positiony - i, self.positionx - i) for i in range(1, 10) if
              0 <= self.positionx < 10 and 0 <= self.positiony < 10]
        dr = [(self.positiony + i, self.positionx + i) for i in range(1, 10) if
              0 <= self.positionx < 10 and 0 <= self.positiony < 10]
        dl = [(self.positiony + i, self.positionx - i) for i in range(1, 10) if
              0 <= self.positionx < 10 and 0 <= self.positiony < 10]

        return ur + ul + dr + dl