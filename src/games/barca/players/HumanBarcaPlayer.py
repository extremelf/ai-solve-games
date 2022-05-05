from games.barca.action import BarcaAction
from games.barca.player import BarcaPlayer
from games.barca.state import BarcaState


class HumanBarcaPLayer(BarcaPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: BarcaState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return BarcaAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: BarcaState):
        pass

    def event_end_game(self, final_state: BarcaState):
        pass
