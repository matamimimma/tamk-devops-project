# map.py
# Map specific operations and variable

class Map:
    def __init__(self):
        self.areas = [
            {
                "name": "area1"
                , "desc": "Area1 description."
                , "items": ["item1"]
                , "move": ["area2", None, None, None]
                        # [north, east, south, west]
            },
            {
                "name": "area2"
                , "desc": "Area2 description."
                , "items": []
                , "move": [None, "area3", "area1", None]
            },
            {
                "name": "area3"
                , "desc": "Area3 description."
                , "items": ["item2", "item3"]
                , "move": [None, None, None, "area2"]
            }
        ]

# Return index of area based on the "name" attribute, if not found return -1
    def get_index(self, area_name):
        for index, map_area in enumerate(self.areas):
            if area_name == map_area["name"]:
                return index
        return -1

# Print area description based on map index
    def print_area_description(self, index):
        indent = " "
        print(
            f"\n{indent:<4} ** {self.areas[index]['name']} **\n"
            f"{self.areas[index]['desc']}\n"
            )

    def print_items_in_area(self, current_pos):
        pass

# test code here
if __name__ == "__main__":
    map = Map()
    map.print_area_description(map.get_index("area3"))
