from games.barca.piece import BarcaPiece


class Lion(BarcaPiece):
    positionx = None
    positiony = None
    legal_moves = []

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

        return {"ur": ur, "ul": ul, "dr": dr, "dl": dl}

    def get_piece_periferics(self) -> list[list]:
        position_ur = [[self.positionx - i, self.positiony + i] for i in range(1) if 0 <= self.positionx - i < 10
                       and 0 <= self.positiony - i < 10]
        position_ul = [[self.positionx - i, self.positiony + i] for i in range(1) if 0 <= self.positionx - i < 10
                       and 0 <= self.positiony - i < 10]
        position_u = [[self.positionx - i, self.positiony] for i in range(1) if 0 <= self.positionx - i < 10
                      and 0 <= self.positiony - i < 10]
        position_d = [[self.positionx + i, self.positiony] for i in range(1) if 0 <= self.positionx - i < 10
                      and 0 <= self.positiony - i < 10]
        position_dr = [[self.positionx + i, self.positiony + i] for i in range(1) if 0 <= self.positionx - i < 10
                       and 0 <= self.positiony - i < 10]
        position_dl = [[self.positionx - i, self.positiony - i] for i in range(1) if 0 <= self.positionx - i < 10
                       and 0 <= self.positiony - i < 10]
        position_l = [[self.positionx, self.positiony - i] for i in range(1) if 0 <= self.positionx - i < 10
                      and 0 <= self.positiony - i < 10]
        position_r = [[self.positionx, self.positiony + i] for i in range(1) if 0 <= self.positionx - i < 10
                      and 0 <= self.positiony - i < 10]

        return position_r + position_l + position_dl + position_dr \
               + position_d + position_ur + position_u + position_ul

    def get_current_pos(self):
        return [self.positionx, self.positiony]

    def set_current_pos(self, posx, posy):
        self.positionx = posx
        self.positiony = posy

    def set_legal_moves(self, moves):
        self.legal_moves = moves

    def get_legal_moves(self):
        return self.legal_moves