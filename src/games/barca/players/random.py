import time

from random import random, randint

from games.barca.action import BarcaAction
from games.barca.player import BarcaPlayer
from games.barca.state import BarcaState


class RandomBarcaPLayer(BarcaPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: BarcaState):
        possible_moves_len = 0
        piece = None
        new_pos = None
        while possible_moves_len == 0:
            piece_index = randint(0, len(state.get_current_player().pieces) - 1)
            piece = self.pieces[piece_index]
            possible_moves = piece.get_legal_moves()
            possible_moves_len = len(possible_moves)
            if possible_moves_len != 0:
                new_pos = possible_moves[randint(0, possible_moves_len-1)]

        action = BarcaAction(piece, new_pos[1], new_pos[0])
        return action

    def event_action(self, pos: int, action, new_state: BarcaState):
        pass

    def event_end_game(self, final_state: BarcaState):
        pass
