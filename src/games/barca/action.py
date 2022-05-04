from piece import BarcaPiece


class BarcaAction:
    __piece: BarcaPiece
    __positionx: int
    __positiony: int

    def __init__(self, piece: BarcaPiece, positionx: int, positiony: int):
        self.__piece = piece
        self.__positiony = positionx
        self.__positionx = positiony

    def get_position(self):
        return [self.__positionx, self.__positiony]

    def get_piece(self):
        return self.__piece
