from games.barca.piece import BarcaPiece


class Elephant(BarcaPiece):
    positionx = None
    positiony = None
    moves = list()

    def __init__(self, name):
        super().__init__(name)

    def initialize_positions(self, x, y):
        if self.positionx is None and self.positiony is None:
            self.positionx = x
            self.positiony = y

    def possible_moves(self):
        ur = [[self.positiony - i, self.positionx + i] for i in range(1, 10) if
              0 <= self.positionx + i < 10 and 0 <= self.positiony - i < 10]
        ul = [[self.positiony - i, self.positionx - i] for i in range(1, 10) if
              0 <= self.positionx - i < 10 and 0 <= self.positiony - i < 10]
        dr = [[self.positiony + i, self.positionx + i] for i in range(1, 10) if
              0 <= self.positionx + i < 10 and 0 <= self.positiony + i < 10]
        dl = [[self.positiony + i, self.positionx - i] for i in range(1, 10) if
              0 <= self.positionx - i < 10 and 0 <= self.positiony + i < 10]

        u = [[self.positiony - i, self.positionx] for i in range(1, 10) if
             0 <= self.positionx < 10 and 0 <= self.positiony - i < 10]
        d = [[self.positiony + i, self.positionx] for i in range(1, 10) if
             0 <= self.positionx < 10 and 0 <= self.positiony + i < 10]
        l = [[self.positiony, self.positionx - i] for i in range(1, 10) if
             0 <= self.positionx - i < 10 and 0 <= self.positiony < 10]
        r = [[self.positiony, self.positionx + i] for i in range(1, 10) if
             0 <= self.positionx + i < 10 and 0 <= self.positiony < 10]

        return ur + ul + dr + dl + u + d + l + r

    def get_current_pos(self) -> list[int]:
        return [self.positionx, self.positiony]

    def get_piece_periferics(self) -> list[int]:
        position_ur = [(self.positionx - 1, self.positiony + 1) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                       and 0 <= self.positiony - 1 < 10]
        position_ul = [(self.positionx - 1, self.positiony + 1) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                       and 0 <= self.positiony - 1 < 10]
        position_u = [(self.positionx - 1, self.positiony) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                      and 0 <= self.positiony - 1 < 10]
        position_d = [(self.positionx + 1, self.positiony) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                      and 0 <= self.positiony - 1 < 10]
        position_dr = [(self.positionx + 1, self.positiony + 1) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                       and 0 <= self.positiony - 1 < 10]
        position_dl = [(self.positionx - 1, self.positiony - 1) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                       and 0 <= self.positiony - 1 < 10]
        position_l = [(self.positionx, self.positiony - 1) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                      and 0 <= self.positiony - 1 < 10]
        position_r = [(self.positionx, self.positiony + 1) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                      and 0 <= self.positiony - 1 < 10]
        position = [(self.positionx, self.positiony) for 1 in range(1) if 0 <= self.positionx - 1 < 10
                    and 0 <= self.positiony - 1 < 10]

        return position + position_r + position_l + position_dl + position_dr + position_d + position_ur + position_u + position_ul

    def set_current_pos(self, posx, posy):
        self.positionx = posx
        self.positiony = posy
