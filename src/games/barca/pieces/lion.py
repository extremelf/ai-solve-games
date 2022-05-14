from games.barca.piece import BarcaPiece


class Lion(BarcaPiece):
    positionx = None
    positiony = None

    def __init__(self, name):
        super().__init__(name)

    def initialize_positions(self, x, y):
        if self.positionx is None and self.positiony is None:
            self.positionx = x
            self.positiony = y

    def get_piece_type(self):
        return self.piece_type

    def possible_moves(self):
        ur = [[self.positiony - i, self.positionx + i] for i in range(1, 10) if
              0 <= self.positionx + i < 10 and 0 <= self.positiony - i < 10]
        ul = [[self.positiony - i, self.positionx - i] for i in range(1, 10) if
              0 <= self.positionx - i < 10 and 0 <= self.positiony - i < 10]
        dr = [[self.positiony + i, self.positionx + i] for i in range(1, 10) if
              0 <= self.positionx + i < 10 and 0 <= self.positiony + i < 10]
        dl = [[self.positiony + i, self.positionx - i] for i in range(1, 10) if
              0 <= self.positionx - i < 10 and 0 <= self.positiony + i < 10]

        return ur + ul + dr + dl

    def get_current_pos(self):
        return [self.positionx, self.positiony]

    def set_current_pos(self, posx, posy):
        self.positionx = posx
        self.positiony = posy

    def set_legal_moves(self, moves):
        self.__legal_moves = moves

    def get_legal_moves(self):
        return self.__legal_moves