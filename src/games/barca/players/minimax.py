import sys

from games.barca.player import BarcaPlayer
from games.barca.player import BarcaResult
from games.barca.state import BarcaState
from games.barca.pieces.elephant import Elephant


class MinimaxBarcaPlayer(BarcaPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.__pieces = [Elephant(),Elephant()]


    def __heuristic(self, state: BarcaState):

        return 10

    def minimax(self, state: BarcaState, depth: int, alpha: int = -sys.maxsize, beta: int = sys.maxsize,
                is_initial_node: bool = True):
        if state.is_finished():
            return {
                BarcaResult.WIN: 4,
                BarcaResult.LOSE: -4
            }[state.get_result(self.get_current_pos())]

        if depth == 0:
            return self.__heuristic(state)

        if self.get_current_pos() == state.get_acting_player():

            value = -sys.maxsize
            selected_post = -1

            for piece in state.get_pieces()