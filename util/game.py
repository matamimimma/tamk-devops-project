# game.py
# Game controlling operations (run game, control stopping, etc.)

class Game:
    def __init__(self):
        self.running = True

# TODO: Build basic run of the game here
    def run_game(self):

        # read user input, trandform to lower case and split into an array
        user_input = input("\n> ").lower().strip().split(" ")

        # only 1-2 word commands allowed
        if len(user_input) > 2:
            print(
                "Unable to process given input. Please use the following"
                "input format: <action> <direction>"
                )
        # set action and target to separate variables
        elif len(user_input) == 1:
            action = user_input[0]
        elif len(user_input) == 2:
            action = user_input[0]
            target = user_input[1]

        if action == "stop":
            self.running = False        # stop game
        else:
            print(user_input.upper())
