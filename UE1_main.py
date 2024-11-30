import numpy as np
from decorator import append

from Classes.Board import Board
from Classes.Game import Game

gamelist = []

for game in range(3):
    game = Game("h2")
    game.find_solution()
    gamelist.append(game)

##TODO multithreaded 100 Games
##TODO console output aks for solved board

gamelist[0].print_shortest_path()








