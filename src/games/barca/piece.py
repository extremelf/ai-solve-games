from abc import abstractmethod


class BarcaPiece:

    def __init__(self, name):
        self.__name = name
        self.__current_pos = None

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_current_pos(self):
        pass

    @abstractmethod
    def set_current_pos(self, posx, posy):
        pass

    @abstractmethod
    def get_piece_periferics(self):
        pass

    @abstractmethod
    def initialize_positions(self, x, y):
        pass

    @abstractmethod
    def possible_moves(self):
        pass

    @abstractmethod
    def set_legal_moves(self, moves):
        pass

    @abstractmethod
    def get_legal_moves(self):
        pass
