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
