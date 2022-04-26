from games.game_simulator import GameSimulator
from games.barca.player import BarcaPlayer
from games.barca.state import BarcaState


class BarcaSimulator(GameSimulator):

    def __init__(self, player1: BarcaPlayer, player2: BarcaPlayer, num_rows: int = 10, num_cols: int = 10):
        super(BarcaSimulator, self).__init__([player1, player2])
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_games(self):
        return BarcaState(self.__num_rows, self.__num_cols)
    
    def before_end_game(self, state: BarcaState):
        pass
    
    def end_game(self, state: BarcaState):
        pass
    