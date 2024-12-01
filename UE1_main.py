import Classes.Multi_stats as perf

###############################

### MAIN FILE ###

#####Test
#new_game = Game("h2")
#new_game.find_solution()
#new_game.print_shortest_path()
#print(new_game.get_complexity_of_solution())

#Choose Parameters
nr_of_games = 3
max_threads = 10

##Start games
result_h1 = perf.start_games(nr_of_games, "h1", max_threads)
result_h2 = perf.start_games(nr_of_games, "h2", max_threads)

##Analyze results
average_h1 = perf.analyze_results(result_h1)
average_h2 = perf.analyze_results(result_h2)

perf.print_results(average_h1, average_h2)

print(f"Total puzzles processed: {len(result_h1)} for H1, {len(result_h2)} for H2")












