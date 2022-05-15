from games.barca.piece import BarcaPiece
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

    # TODO verificar se o movimento gera perigo para a peça
    # Retorna se o movimento coloca perigo

    def get_periferics(self, x, y) -> list[list]:
        position_ur = [[x - i, y + i] for i in range(1) if 0 <= x - i < 10
                       and 0 <= y - i < 10]
        position_ul = [[x - i, y + i] for i in range(1) if 0 <= x - i < 10
                       and 0 <= y - i < 10]
        position_u = [[x - i, y] for i in range(1) if 0 <= x - i < 10
                      and 0 <= y - i < 10]
        position_d = [[x + i, y] for i in range(1) if 0 <= x - i < 10
                      and 0 <= y - i < 10]
        position_dr = [[x + i, y + i] for i in range(1) if 0 <= x - i < 10
                       and 0 <= y - i < 10]
        position_dl = [[x - i, y - i] for i in range(1) if 0 <= x - i < 10
                       and 0 <= y - i < 10]
        position_l = [[x, y - i] for i in range(1) if 0 <= x - i < 10
                      and 0 <= y - i < 10]
        position_r = [[x, y + i] for i in range(1) if 0 <= x - i < 10
                      and 0 <= y - i < 10]
        position = [[x, y] for i in range(1) if 0 <= x - i < 10
                    and 0 <= y - i < 10]

        return position + position_r + position_l + position_dl + position_dr \
               + position_d + position_ur + position_u + position_ul

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

    def is_in_fear(self, piece_type, periferics):
        # TODO verificar periferia da peça atual e verificar se existe perigo e se ira ficar em perigo
        # algum oponente nessas coordenadas retorna true or false caso exista um destes tipos a acontecer
        # com base se está em perigo
        # novos argumentos, lista das perifierias e o tipo de peça que é

        # Need to check how will it be around it
        opponent = self.__players[self.__acting_player]

        for pieces_opo in opponent.pieces:
            current_pos_oppo = pieces_opo.get_current_pos()
            if current_pos_oppo in periferics:
                if isinstance(piece_type, Elephant):
                    if isinstance(pieces_opo, Mouse):
                        return True
                if isinstance(piece_type, Mouse):
                    if isinstance(pieces_opo, Lion):
                        return True
                if isinstance(piece_type, Lion):
                    if isinstance(pieces_opo, Elephant):
                        return True

        return False

    def step_above_others(self, piece):

        player = self.__players[1] if self.__acting_player == 0 else self.__players[0]
        opponent = self.__players[self.__acting_player]
        all_pieces = player.pieces.get_current_pos() + opponent.pieces.get_current_pos()  # posiçao atual de todas as as peças no tabuleiro
        possible_moves = piece.possible_moves()
        for direction_index in possible_moves:
            if possible_moves[direction_index] in all_pieces:
                for move in possible_moves[direction_index]:
                    if move in all_pieces:
                        if direction_index == "ur":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[1] < position[0] < 10 and move[0] > position[1] >= 0,
                                       possible_moves[direction_index]))
                        if direction_index == "ul":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[1] > position[0] >= 0 and move[0] > position[1] >= 0,
                                       possible_moves[direction_index]))
                        if direction_index == "dr":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[1] < position[0] < 10 and move[0] < position[1] <= 9,
                                       possible_moves[direction_index]))
                        if direction_index == "dl":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[1] > position[0] >= 0 and move[0] > position[1] >= 0,
                                       possible_moves[direction_index]))
                        if direction_index == "u":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[0] > position[1] >= 0,
                                       possible_moves[direction_index]))
                        if direction_index == "d":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[0] < position[1] <= 9,
                                       possible_moves[direction_index]))
                        if direction_index == "r":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[1] < position[0] < 10,
                                       possible_moves[direction_index]))
                        if direction_index == "l":
                            possible_moves[direction_index] = list(
                                filter(lambda position: move[1] > position[0] >= 0,
                                       possible_moves[direction_index]))

        return possible_moves


def get_legal_moves(self):
    # verificar se as peças estão in fear ex do resultado {0:{true}, 1:{False},...}
    # next step caso existe pelo menos 1 True remove todos os falsos e irá apenas verificar jogadas
    # válidas para este
    # array resultante

    # ciclo for deste novo array e para cada possible move da peça atual verifica se não vai ficar em medo,
    # chamando
    # a nova função que retornará um True or false, com base neste return, mantém a peça nos possible moves ou remove

    pieces_fear = {}

    acting_player = self.__players[1] if self.__acting_player == 0 else self.__players[0]

    # population dictionary with the index and respective values
    for piece_index in range(0, len(acting_player.pieces)):
        piece = acting_player.pieces[piece_index]
        pieces_fear[piece_index] = self.is_in_fear(isinstance(piece, Elephant), piece.get_piece_periferics())

        # remove those with false as a value if at least one is true
        for index in pieces_fear:
            if pieces_fear[index]:
                pieces_fear = dict(filter(lambda value: value[1], pieces_fear.items()))

        # Not to step over the other
        for index2 in pieces_fear:
            piece = acting_player.pieces[index2]
            pieces_fear[index2] = self.step_above_others(piece)

        for piece_index in pieces_fear:
            valid_moves = []
            for move in pieces_fear[piece_index]:
                periferics = self.get_periferics(move[1], move[0])
                if self.is_in_fear(piece.get_piece_type(), periferics):
                    valid_moves.append(move)
            acting_player.pieces[piece_index].set_legal_moves(valid_moves)


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
