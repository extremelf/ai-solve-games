from enum import Enum


class BarcaPiece(Enum):

    Elephant = 0
    Mice = 1
    Lion = 2

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value

    def __str__(self):
        return {
            0: "E",
            1: "M",
            2: "L"
        }[self.value]
