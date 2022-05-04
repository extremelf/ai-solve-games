from games.state import State
from piece import BarcaPiece
from player import BarcaPlayer

"player->pieces->coordenadas"


class BarcaState(State):
    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 10, num_cols: int = 10):
        super().__init__()

        self.__num_rows = num_rows
        self.__num_cols = num_cols

        self.__grid = [BarcaState.EMPTY_CELL for _i in range(self.__num_cols) for _j in range(self.__num_rows)]

        # Places the pieces in the board, very initial way
        self.__grid[4] = BarcaPiece.Elephant.__str__()
        self.__grid[5] = BarcaPiece.Elephant.__str__()
        self.__grid[94] = BarcaPiece.Elephant.__str__()
        self.__grid[95] = BarcaPiece.Elephant.__str__()

        self.__grid[13] = BarcaPiece.Lion.__str__()
        self.__grid[16] = BarcaPiece.Lion.__str__()
        self.__grid[86] = BarcaPiece.Lion.__str__()
        self.__grid[83] = BarcaPiece.Lion.__str__()

        self.__grid[14] = BarcaPiece.Mice.__str__()
        self.__grid[15] = BarcaPiece.Mice.__str__()
        self.__grid[84] = BarcaPiece.Mice.__str__()
        self.__grid[85] = BarcaPiece.Mice.__str__()

        self.__turns_count = 1

        self.__action_player = 0

        self.__has_winner = False

    def get_grid(self):
        return self.__grid

    def get_opponent_cords(self, player):
        opponent_pieces_coords = player.pieces.get_current_position



    def get_legal_moves(self, piece, opponent_pieces_coords):

        all_moves = piece.possible_moves

        ilegal_coords = opponent_pieces_coords

        for moves in all_moves:
            if moves in ilegal_coords:
                all_moves.remove(moves)

        return moves
