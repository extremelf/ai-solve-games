from games.barca.piece import BarcaPiece


class Mouse(BarcaPiece):
    position_x = None
    position_y = None
    list_moves = list()

    def __init__(self, name):
        super().__init__(name)

    def initialize_positions(self, x, y):
        if self.position_x and self.position_y is None:
            self.position_x = x
            self.position_y = y

    def possible_moves(self):
        u = [(self.position_y + i, self.position_x + i) for i in range(1, 10) if 0 <= self.position_y < 10 and
             0 <= self.position_x < 10]
