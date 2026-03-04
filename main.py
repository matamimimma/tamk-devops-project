# main.py
# start game here

from util.game import Game
from util.map import Map
from util.player import Player
from util.items import Items

if __name__ == "__main__":

    start_pos = 0

    map = Map()
    items = Items()
    player = Player(start_pos)
    game = Game(map, player)

    print("-- START --")
    map.print_area_description(player.position_index)

    while game.running:
        game.run_game()

    print("-- STOPPED --")
