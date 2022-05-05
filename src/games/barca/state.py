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
        return True

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
                    grid[current_pos[1]][current_pos[0]-1] = 2
                elif isinstance(piece, Lion):
                    grid[current_pos[1]][current_pos[0]-1] = 3
                elif isinstance(piece, Mouse):
                    grid[current_pos[1]][current_pos[0]-1] = 4

        self.display_grid(grid)

    def display_grid(self, grid):

        self.__displayer_separator()
        self.__displayer_numbers()

        for row in range(0, self.__num_rows):
            print(row, end="")
            print("|", end="")
            for col in range(0, self.__num_cols):
                self.__displayer_cell(row, col)
                print("|", end="")
            print("")
            self.__displayer_separator()
        self.__displayer_numbers()
        print("")
        #for pos in range(len(grid)):
         #   if pos % 10 == 9:
          #      print(f' {grid[pos]}', end="\n")
           # else:
            #    print(f' {grid[pos]}', end=" ")

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

    def __displayer_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(f' {col} ', end="")
        print("")

    def get_opponent_cords(self, player):
        opponent_pieces_coords = player.pieces.get_current_position

    def get_legal_moves(self, piece, opponent_pieces_coords):

        all_moves = piece.possible_moves

        ilegal_coords = opponent_pieces_coords

        for moves in all_moves:
            if moves in ilegal_coords:
                all_moves.remove(moves)

        return moves

    def before_results(self):
        pass

    def get_num_players(self):
        pass

    def get_result(self, pos):
        pass

    def is_finished(self) -> bool:
        pass

    def validate_action(self, action) -> bool:
        pass
