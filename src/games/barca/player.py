from abc import ABC

from games.player import Player
from games.barca.result import BarcaResult
from games.barca.pieces.elephant import Elephant
from games.barca.pieces.lion import Lion
from games.barca.pieces.mouse import Mouse


class BarcaPlayer(Player, ABC):

    def __init__(self, name):
        super().__init__(name)
        self.pieces = [Elephant("elephant"), Elephant("elephant"), Lion("lion"), Lion("lion"), Mouse("mouse"),
                       Mouse("mouse")]

        self.__stats = {}
        for bres in BarcaResult:
            self.__stats[bres] = 0

        self.__num_games = 0

    def print_stats(self):
        num_wins = self.__stats[BarcaResult.WIN]
        print(f"Player {self.get_name()}: {num_wins}/{self.__num_games} wins ({num_wins * 100 / self.__num_games} win "
              f"rate")

    def event_new_game(self):
        self.__num_games += 1

    def event_result(self, pos: int, result: BarcaResult):
        if pos == self.get_current_pos():
            self.__stats[result] += 1
