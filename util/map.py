# map.py
# Map specific operations and variable

class Map:
    def __init__(self):
        self.areas = [
            {
                "name": "area1"
                , "desc": "Area1 description."
                , "move": ["area2", None, None, None]
                        # [north, east, south, west]
            },
            {
                "name": "area2"
                , "desc": "Area2 description."
                , "move": [None, "area3", "area1", None]
            },
            {
                "name": "area2"
                , "desc": "Area2 description."
                , "move": [None, None, None, "area2"]
            }
        ]

# Return index of area based on the "name" attribute, if not found return -1
    def get_index(self, area_name):
        for index, map_area in enumerate(self.areas):
            if area_name == map_area["name"]:
                return index
        return -1

# test code here
if __name__ == "__main__":
    map = Map()
    print(map.get_index("area1"))
