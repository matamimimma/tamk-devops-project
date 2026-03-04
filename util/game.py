# game.py
# Game controlling operations (run game, control stopping, etc.)

class Game:
    def __init__(self, map, player, items):
        self.running = True
        self.commands = ["stop", "go", "take", "drop", "inventory", "investigate"]
        self.map = map
        self.player = player
        self.items = items

# TODO: Build basic run of the game here
    def run_game(self):

        current_pos = self.map.areas[self.player.position_index]

        # read user input, trandform to lower case and split into an array
        user_input = input("\n> ").lower().strip().split(" ")

        # only 1-2 word commands allowed
        if len(user_input) > 2:
            print(
                "\nUnable to process given input. Please use the following"
                "\ninput format: <action> <direction>"
                )
            return
        # set action and target to separate variables
        elif len(user_input) == 1:
            action = user_input[0]
        elif len(user_input) == 2:
            action = user_input[0]
            target = user_input[1]

        if action in self.commands:
            if action == "stop":
                self.running = False        # stop game
            elif action == "go":
                self.player.move(self.map, current_pos, target)
            elif action == "take":
                self.player.pick_up(target, current_pos, self.map, self.items)
            elif action == "drop":
                self.player.drop(target, self.map, self.items)
            elif action == "inventory":
                self.player.print_inventory()
            elif action == "investigate":
                self.map.print_items_in_area(self.player.position_index)

        elif action in self.player.item_commands:
            self.player.do_item_action(action, target, self.items)

        else:
            print("Action not regognised.")

# Print game instructions
    def print_help(self):
        print(
            "\nPlease use the following input format: <action> <direction>"
            )
        pass
