from abc import abstractmethod


class BarcaPiece:

    def __init__(self, name):
        self.__name = name
        self.__current_pos = None

    def get_name(self):
        return self.__name

    def get_current_pos(self):
        return self.__current_pos

    def set_current_pos(self, new_pos):
        self.__current_pos = new_pos

    @abstractmethod
    def initialize_positions(self, x, y):
        pass

    @abstractmethod
    def get_legal_moves(self, state):
        pass
