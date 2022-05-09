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
            piece_index = int(input(f'Player{state.get_acting_player(), self.get_name()}, choose a piece:'))
            while piece_index not in range(0, len(self.pieces)):
                piece_index = int(input(f'Invalid piece, choose a piece:'))
            piece_pos_x = int(input(f'Player{state.get_acting_player()}, choose a x position:'))
            while piece_pos_x not in range(0, 9):
                piece_pos_x = int(input(f'Invalid position, choose a position:'))
            piece_pos_y = int(input(f'Player{state.get_acting_player()}, choose a y position:'))
            while piece_pos_y not in range(0, 9):
                piece_pos_y = int(input(f'Invalid position, choose a position:'))
            possible_moves = self.pieces[piece_index].possible_moves()
            print(possible_moves)
            while [piece_pos_y, piece_pos_x] not in possible_moves:
                print("Invalid move")
                piece_pos_x = int(input(f'Player{state.get_acting_player()}, choose a x position:'))
                while piece_pos_x not in range(0, 9):
                    piece_pos_x = int(input(f'Invalid position, choose a position:'))
                piece_pos_y = int(input(f'Player{state.get_acting_player()}, choose a y position:'))
                while piece_pos_y not in range(0, 9):
                    piece_pos_y = int(input(f'Invalid position, choose a position:'))

            try:
                return BarcaAction(self.pieces[piece_index], piece_pos_x, piece_pos_y)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: BarcaState):
        pass

    def event_end_game(self, final_state: BarcaState):
        pass
