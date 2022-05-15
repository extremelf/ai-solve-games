from games.barca.players.HumanBarcaPlayer import HumanBarcaPLayer
from games.barca.simulator import BarcaSimulator
from games.connect4.players.greedy import GreedyConnect4Player
from games.connect4.players.luis_fernandes_player import LuisFernandesPlayer
from games.game_simulator import GameSimulator
from games.poker.players.always_bet_king import AlwaysBetKingKuhnPokerPlayer
from games.poker.players.luis_fernandes_player import LuisFernandesKuhnPlayer
from games.barca.players.minimax import MinimaxBarcaPlayer
from games.barca.players.Greedy import GreedyBarcaPlayer
from games.barca.players.random import RandomBarcaPLayer


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1000

    # for sim in c4_simulations:
    #    run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)

    # for sim in poker_simulations:
    #   run_simulation(sim["name"], KuhnPokerSimulator(sim["player1"], sim["player2"]), num_iterations)

    run_simulation("teste", BarcaSimulator(HumanBarcaPLayer("José"), HumanBarcaPLayer("Joaquim")), 1000)


if __name__ == "__main__":
    main()
