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

# Print items in area based on map index
    def print_items_in_area(self, index):
        indent = " "
        print("Collectible items in area:")
        for item in self.areas[index]["items"]:
            print(f"{indent:<4} {item}")

# Remove items from area when picked up
    def remove_from_area(self, item, pos_index):
        self.areas[pos_index]["items"].remove(item)

# Add item to area when dropped
    def add_to_area(self, item, pos_index):
        pass

# test code here
if __name__ == "__main__":
    map = Map()
    map.print_area_description(map.get_index("area3"))
    map.print_items_in_area(map.get_index("area3"))
