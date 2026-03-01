# player.py
# Player specific operations and variables

from map import Map

class Player:
    def __init__(self, area_index):
        self.position_index = area_index
        self.inventory = []

# Change area on a map
    def move(self, target_dir):
        # possible directions used in game
        directions =["north", "east", "south", "west"]

        if target_dir in directions:
            # 0: north, 1:east, 2:south, 3:west
            dir_index = directions.index(target_dir)

            # TODO:
            # 1. check if direction possible from current pos
            # 2. -> change player position

# Test code here
if __name__ == "__main__":
    map = Map()
    start_pos = map.get_index("area1")
    player = Player(start_pos)

    print(player.position_index)
    map.print_area_description(player.position_index)
    pass
