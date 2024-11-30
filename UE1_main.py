##TODO multithreaded 100 Games
##TODO console output ask for solved board
##TODO table with complexity comparisons of different heuristics
##TODO comment code
##TODO rework documentation

from Classes.Game import Game

number_of_boards : int = 0

gamelist = []

for game in range(2):
    game = Game("h1")
    game.find_solution()
    gamelist.append(game)



gamelist[0].print_shortest_path()
print(gamelist[0].get_complexity_of_solution())

##TODO split into different complexities
for game in gamelist:
    number_of_boards += game.get_number_of_Boards()

print(number_of_boards / 2)







