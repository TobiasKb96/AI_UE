##TODO multithreaded 100 Games
##TODO console output ask for solved board
##TODO table with complexity comparisons of different heuristics
##TODO comment code -> Julian
##TODO rework documentation ->Julian

from Classes.Game import Game

number_of_boards : int = 0

gamelist = []

for game in range(1):
    game = Game("h2")
    game.find_solution()
    gamelist.append(game)



gamelist[0].print_shortest_path()
print(gamelist[0].get_complexity_of_solution())
print(gamelist[0].get_number_of_Boards())


##TODO split into different complexities








