from games.barca.piece import BarcaPiece


class Mouse(BarcaPiece):
    positionx = None
    positiony = None
    __legal_moves = None

    def __init__(self, name):
        super().__init__(name)

    def initialize_positions(self, x, y):
        if self.positionx is None and self.positiony is None:
            self.positionx = x
            self.positiony = y

    def get_piece_type(self):
        return self.piece_type

    def possible_moves(self):
        u = [[self.positiony - i, self.positionx] for i in range(1, 10) if
             0 <= self.positiony - i < 10 and 0 <= self.positionx < 10]
        d = [[self.positiony + i, self.positionx] for i in range(1, 10) if
             0 <= self.positiony + i < 10 and 0 <= self.positionx < 10]
        l = [[self.positiony, self.positionx - i] for i in range(1, 10) if
             0 <= self.positiony < 10 and 0 <= self.positionx - i < 10]
        r = [[self.positiony, self.positionx + i] for i in range(1, 10) if
             0 <= self.positiony < 10 and 0 <= self.positionx + i < 10]

        return {"u": u, "d": d, "l": l, "r": r}

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
        position = [[self.positionx, self.positiony] for i in range(1) if 0 <= self.positionx - i < 10
                    and 0 <= self.positiony - i < 10]

        return position + position_r + position_l + position_dl + position_dr \
               + position_d + position_ur + position_u + position_ul

    def get_current_pos(self):
        return [self.positionx, self.positiony]

    def set_current_pos(self, posx, posy):
        self.positionx = posx
        self.positiony = posy

    def set_legal_moves(self, moves):
        self.__legal_moves = moves

    def get_legal_moves(self):
        return self.__legal_moves
