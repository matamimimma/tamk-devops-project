# items.py
# Game items

class Items:
    def __init__(self):
        self.all = {
            "item1": {
                "desc": "Item1 description"
                , "action": "use"
                , "action_desc": "Item1 used"
            },
            "item2": {
                "desc": "Item2 description"
                , "action": None
                , "action_desc": None
            },
            "item3": {
                "desc": "Item3 description"
                , "action": None
                , "action_desc": None
            }
        }

# Print items description
    def print_item_description(self, item):
        print(f"{item:<15} - {self.all[item]['desc']}")

# Print items action description
    def print_action_decription(self):
        pass

# TEST code here
if __name__ == "__main__":
    items = Items()
    inv = ["item1", "item3"]

    for item in inv:
        if item in items.all:
            items.print_item_description(item)
