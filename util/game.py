# game.py
# Game controlling operations (run game, control stopping, etc.)

class Game:
    def __init__(self):
        self.running = True

# TODO: Build basic run of the game here
    def run_game(self):

        # read user input, trandform to lower case and split into an array
        user_input = input("\n> ").lower().strip().split(" ")

        if user_input.lower() == "stop":
            self.running = False        # stop game
        else:
            print(user_input.upper())
