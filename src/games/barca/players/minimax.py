import sys
from random import random, randint

from games.barca.action import BarcaAction
from games.barca.player import BarcaPlayer
from games.barca.player import BarcaResult
from games.barca.state import BarcaState


class MinimaxBarcaPlayer(BarcaPlayer):
    def __init__(self, name):
        super().__init__(name)

    def __heuristic(self, state: BarcaState):

        return randint(0, 10000)

    def minimax(self, state: BarcaState, depth: int, alpha: int = -sys.maxsize, beta: int = sys.maxsize,
                is_initial_node: bool = True):
        if state.is_finished():
            return {
                BarcaResult.WIN: 40000000,
                BarcaResult.LOSE: -40000000
            }[state.get_result(self.get_current_pos())]

        if depth == 0:
            return self.__heuristic(state)

        if self.get_current_pos() == state.get_acting_player():

            value = -sys.maxsize
            selected_move = None

            for piece in state.get_current_player().pieces:
                possible_moves = piece.get_legal_moves()
                current_pos = piece.get_current_pos()
                if [current_pos[1], current_pos[0]] in possible_moves:
                    print("WHY IN DA FUCK")
                for move in possible_moves:
                    action = BarcaAction(piece, move[1], move[2])
                    if state.validate_action(action):
                        previous_a = value
                        next_state = state.clone()
                        next_state.play(action)
                        value = max(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                        alpha = max(alpha, value)

                        if value >= previous_a:
                            selected_move = action
                        if alpha >= beta:
                            break
            if is_initial_node:
                return selected_move
            return value
        else:
            value = sys.maxsize
            for piece in state.get_oponent_player().pieces:
                possible_moves = piece.possible_moves()
                for move in possible_moves:
                    action = BarcaAction(piece, move[1], move[0])
                    if state.validate_action(action):
                        next_state = state.clone()
                        next_state.play(action)
                        value = min(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                        beta = min(beta, value)
                        if beta <= alpha:
                            break
            return value

    def get_action(self, state: BarcaState):
        move = self.minimax(state, 3)
        print(move.get_position(), move.get_piece())
        return move

    def event_action(self, pos: int, action, new_state: BarcaState):
        # ignore
        pass

    def event_end_game(self, final_state: BarcaState):
        # ignore
        pass
