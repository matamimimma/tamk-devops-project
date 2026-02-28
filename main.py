# main.py
# start game here

from util.game import Game

if __name__ == "__main__":
    game = Game()

    print("-- START --")

    while game.running:
        game.run_game()

    print("-- STOPPED --")
