# player.py
# Player specific operations and variables

from map import Map

class Player:
    def __init__(self, area_index):
        self.position_index = area_index
        self.inventory = []

# Change area on a map
    def move(self):
        pass

# Test code here
if __name__ == "__main__":
    map = Map()
    start_pos = map.get_index("area1")
    player = Player(start_pos)

    print(player.position_index)
    map.print_area_description(player.position_index)
    pass
