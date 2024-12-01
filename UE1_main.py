##TODO multithreaded 100 Games
##TODO console output ask for solved board
##TODO table with complexity comparisons of different heuristics
##TODO comment code -> Julian
##TODO rework documentation ->Julian

from Classes.Game import Game

number_of_boards : int = 0

gamelist = []

# Loop to create x game instances
for game in range(1):
    # Input: "h1" specifies the Hamming heuristic; "h2" specifies the Manhattan heuristic
    # Output: Initialized `Game` instance
    game = Game("h2")
    # Function: Finds the solution for the given board and heuristic using A*
    game.find_solution()
    # Function: Add the solved game to the list of games
    gamelist.append(game)


# Function: Print the solution part of a given solution
gamelist[0].print_shortest_path()
print(gamelist[0].get_complexity_of_solution())
print(gamelist[0].get_number_of_Boards())


##TODO split into different complexities








