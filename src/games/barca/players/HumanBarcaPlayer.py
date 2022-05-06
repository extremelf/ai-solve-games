from games.barca.action import BarcaAction
from games.barca.player import BarcaPlayer
from games.barca.state import BarcaState


class HumanBarcaPLayer(BarcaPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: BarcaState):
        state.display()
        print("Pieces: ")
        state.display_acting_player_pieces()
        while True:
            piece_index = int(input(f'Player{state.get_acting_player()}, choose a piece:'))
            while piece_index not in range(0, len(self.pieces)):
                piece_index = int(input(f'Invalid piece, choose a piece:'))

            try:
                return BarcaAction(self.pieces[piece_index], 3, 4)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: BarcaState):
        pass

    def event_end_game(self, final_state: BarcaState):
        pass
