from abc import ABC

from games.barca.pieces.lion import Lion
from games.barca.pieces.mouse import Mouse
from games.game_simulator import GameSimulator
from games.barca.player import BarcaPlayer
from games.barca.state import BarcaState
from games.barca.pieces.elephant import Elephant


class BarcaSimulator(GameSimulator, ABC):

    def __init__(self, player1: BarcaPlayer, player2: BarcaPlayer, num_rows: int = 10, num_cols: int = 10):
        super(BarcaSimulator, self).__init__([player1, player2])
        self.init_pieces(player1, 1, 0)
        self.init_pieces(player2, -1, 1)

        self.__players = [player1, player2]
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    @staticmethod
    def init_pieces(player, multiplier, offset):
        elephants = [piece for piece in player.pieces if isinstance(piece, Elephant)]
        lions = [piece for piece in player.pieces if isinstance(piece, Lion)]
        mice = [piece for piece in player.pieces if isinstance(piece, Mouse)]

        for piece in range(len(elephants)):
            if piece == 1:
                elephants[piece].initialize_positions(5, (5 + (multiplier * (offset + 4))))
            else:
                elephants[piece].initialize_positions(6, (5 + (multiplier * (offset + 4))))
        for piece in range(len(lions)):
            if piece == 1:
                lions[piece].initialize_positions(4, (5 + (multiplier * (offset + 3))))
            else:
                lions[piece].initialize_positions(7, (5 + (multiplier * (offset + 3))))
        for piece in range(len(mice)):
            if piece == 1:
                mice[piece].initialize_positions(5, (5 + (multiplier * (offset + 3))))
            else:
                mice[piece].initialize_positions(6, (5 + (multiplier * (offset + 3))))

    def init_games(self):
        return BarcaState(self.__num_rows, self.__num_cols, self.__players)

    def before_end_game(self, state: BarcaState):
        pass

    def end_game(self, state: BarcaState):
        pass
