from games.barca.result import BarcaResult
from games.state import State
from games.barca.player import BarcaPlayer
from games.barca.action import BarcaAction
import copy
from games.barca.pieces.elephant import Elephant
from games.barca.pieces.lion import Lion
from games.barca.pieces.mouse import Mouse

"player->pieces->coordenadas"


class BarcaState(State):
    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 10, num_cols: int = 10, players: list[BarcaPlayer] = None):
        super().__init__()

        self.__players = players
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        self.__grid = [[BarcaState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        self.__turns_count = 1

        self.__acting_player = 0

        self.__has_winner = False

    def get_grid(self):
        return self.__grid

    def get_acting_player(self) -> int:
        return self.__acting_player

    def __check_winner(self):
        occupied_holes = 0
        holes_pos = [[3, 3], [3, 6], [6, 3], [6, 6]]
        for piece in self.__players[1 if self.__acting_player == 0 else 0].pieces:
            pos = piece.get_current_pos()
            if [pos[1], pos[0]] in holes_pos:
                occupied_holes += 1
        if occupied_holes >= 3:
            return True
        return False

    def update(self, action: BarcaAction):
        piece = action.get_piece()
        new_position = action.get_position()

        piece.set_current_pos(new_position[0], new_position[1])

        self.__has_winner = self.__check_winner()

        self.__acting_player = 1 if self.__acting_player == 0 else 0

    def clone(self):
        new_state = copy.deepcopy(self)
        return new_state

    def display(self):
        grid = self.__grid
        for player in self.__players:
            for piece in player.pieces:
                current_pos = piece.get_current_pos()
                if isinstance(piece, Elephant):
                    grid[current_pos[1]][current_pos[0]] = 2
                elif isinstance(piece, Lion):
                    grid[current_pos[1]][current_pos[0]] = 3
                elif isinstance(piece, Mouse):
                    grid[current_pos[1]][current_pos[0]] = 4


        self.display_grid(grid)

    def get_opponent_cords(self):
        # opponent_pieces_coords = player.pieces.get_current_position

        opponent = self.__players[1] if self.__action_player == 0 else self.__players[0]

        opponent_cords = []
        for piece in opponent.pieces:
            current_pos = piece.get_current_pos()
            opponent_cords.__add__(current_pos)
        return opponent_cords

    def is_in_fear(self):

        # Need to check how will it be arround it
        opponent = self.__players[1] if self.__action_player == 0 else self.__players[0]

        for pieces in self.__acting_player:
            current_pos = pieces.get_current_pos()
            current_pos = [self.position]

        #
        # if self.__acting_player.pieces[Elephant].get_current_pos() == (opponent.pieces[Mouse].get_current_pos()+1):
        #     legal_moves = self.__acting_player.pieces[Elephant].possible_moves()
        # elif self.__acting_player.pieces[Lion].get_current_pos() == (opponent.pieces[Elephant].get_current_pos()+1):
        #     legal_moves = self.__acting_player.pieces[Lion].possible_moves()
        # elif self.__acting_player.pieces[Mouse].get_current_pos() == (opponent.pieces[Lion].get_current_pos() + 1):
        #     legal_moves = self.__acting_player.pieces[Mouse].possible_moves()

    def display_grid(self, grid):

        self.__displayer_separator()
        self.__display_numbers()
        for row in range(0, self.__num_rows):
            print(row, end="")
            print("|", end="")
            for col in range(0, self.__num_cols):
                self.__displayer_cell(row, col)
                print("|", end="")
            print("")
            self.__displayer_separator()

        self.__display_numbers()
        print("")

    def __displayer_cell(self, row, col):
        print({
                  2: ' E ',
                  3: ' L ',
                  4: ' M ',
                  BarcaState.EMPTY_CELL: '   '
              }[self.__grid[row][col]], end="")

    def __displayer_separator(self):
        for col in range(0, self.__num_cols):
            print("----", end="")
        print("---")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print('  ', end="")
            print(f' {col}', end="")
        print("")

    def get_legal_moves(self, piece):

        all_moves = piece.possible_moves()

        opponent = self.__players[1] if self.__action_player == 0 else self.__players[0]
        legal_moves = []
        opponent_cords = []
        for piece in opponent.pieces:
            current_pos = piece.get_current_pos()
            opponent_cords.__add__(current_pos)
            for opponent_cords in all_moves:
                if opponent_cords in all_moves:
                    all_moves.remove(opponent_cords)
                    legal_moves = all_moves
        return legal_moves

    def display_acting_player_pieces(self):
        player = self.__players[1 if self.__acting_player == 0 else 0]
        for index in range(len(player.pieces)):
            piece = player.pieces[index]
            piece_pos = piece.get_current_pos()
            print(f'{index}: {piece.get_name()} ({piece_pos[0]}, {piece_pos[1]})')

    def before_results(self):
        pass

    def get_num_players(self):
        pass

    def get_result(self, pos):
        if self.__has_winner:
            return BarcaResult.LOSE if pos == self.__acting_player else BarcaResult.WIN
        return None

    def is_finished(self) -> bool:
        return self.__has_winner

    def validate_action(self, action) -> bool:
        return True
