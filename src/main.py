from games.barca.players.HumanBarcaPlayer import HumanBarcaPLayer
from games.barca.players.random import RandomBarcaPLayer
from games.barca.simulator import BarcaSimulator
from games.game_simulator import GameSimulator


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

    run_simulation("teste", BarcaSimulator(HumanBarcaPLayer("José"), RandomBarcaPLayer("Joaquim")), 25)


if __name__ == "__main__":
    main()
