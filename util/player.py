# player.py
# Player specific operations and variables

from util.map import Map

class Player:
    def __init__(self, area_index):
        self.position_index = area_index
        self.inventory = []

# Change area on a map
# current_pos = area block from map
# target_dir = string
    def move(self, map, current_pos, target_dir):
        # possible directions used in game
        directions =["north", "east", "south", "west"]

        if target_dir in directions:
            # target direction index (0: north, 1:east, 2:south, 3:west)
            dir_index = directions.index(target_dir)
            new_pos_name = current_pos["move"][dir_index]

            if new_pos_name == None:
                # moving direction not possible
                print("Not possible")
            else:
                # iterate area_map and check for matching name
                for area in map.areas:
                    if area["name"] == new_pos_name:
                        # update position_index to new position
                        self.position_index = map.areas.index(area)
                        map.print_area_description(self.position_index)
                    else:
                        continue
        else:
            print("Direction not recognised")

# Pick up items
    def pick_up(self, target, current_pos, map):
        in_area = False     # item found in area

        # find matching item in area
        for item in current_pos["items"]:
            if item.lower() == target:
                in_area = True      # match found

                self.inventory.append(item)
                # remove pick up item from area
                map.remove_from_area(item, self.position_index)

                print(f"Picked up item: {item}")
            else:
                continue

        if not in_area:
            print(f"Item not found in area: {target}")

# Drop items
    def drop(self, target):
        for item in self.inventory:
            if item.lower() == target:
                self.inventory.remove(item)
                print(f"Item dropped: {item}")
            else:
                continue

# Test code here
if __name__ == "__main__":
    map = Map()
    start_pos = map.get_index("area1")
    player = Player(start_pos)

    player.pick_up("item1", map.areas[player.position_index], map)

    print(player.inventory)
    print(map.areas[player.position_index])
