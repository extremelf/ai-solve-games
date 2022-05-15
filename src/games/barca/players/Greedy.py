import sys
from random import choice

import random

from games.barca.action import BarcaAction
from games.barca.player import BarcaPlayer
from games.barca.state import BarcaState


class GreedyBarcaPlayer(BarcaPlayer):
    def __init__(self, name):
        super().__init__(name)

    def __heuristic(self, posx, posy):
        grid = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                [10, 25, 25, 25, 25, 25, 25, 25, 25, 10],
                [10, 25, 50, 50, 50, 50, 50, 50, 25, 10],
                [10, 25, 50, 100, 75, 75, 100, 50, 25, 10],
                [10, 25, 50, 75, 75, 75, 75, 50, 25, 10],
                [10, 25, 50, 75, 75, 75, 75, 50, 25, 10],
                [10, 25, 50, 100, 75, 75, 100, 50, 25, 10],
                [10, 25, 50, 50, 50, 50, 50, 50, 25, 10],
                [10, 25, 25, 25, 25, 25, 25, 25, 25, 10],
                [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]

        return grid[posy][posx]

    def get_action(self, state: BarcaState):
        value = -sys.maxsize
        selected_move = None
        for piece in self.pieces:
            piece_pos = piece.get_current_pos()
            for move in piece.possible_moves():
                temp_value = self.__heuristic(move[1], move[0])
                if temp_value is not self.__heuristic(piece_pos[0], piece_pos[1]) and temp_value >= value:
                    value = temp_value
                    selected_move = BarcaAction(piece, move[1], move[0])

        return selected_move

    def event_action(self, pos: int, action, new_state: BarcaState):
        pass

    def event_end_game(self, final_state: BarcaState):
        pass
