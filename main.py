# main.py
# start game here

from util.game import Game
from util.map import Map
from util.player import Player

if __name__ == "__main__":
    game = Game()

    print("-- START --")

    while game.running:
        game.run_game()

    print("-- STOPPED --")
