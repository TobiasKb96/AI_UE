##TODO multithreaded 100 Games
##TODO console output ask for solved board
##TODO table with complexity comparisons of different heuristics
##TODO comment code -> Julian
##TODO rework documentation ->Julian
import concurrent
import threading
import time
import concurrent.futures
from collections import defaultdict

from Classes.Game import Game






###############################


#####Test
#new_game = Game("h2")
#new_game.find_solution()
#new_game.print_shortest_path()
#print(new_game.get_complexity_of_solution())
nr_of_games = 100

def solve_puzzle(instance_id, heuristic_method="h1"):
    ##Measure run time
    start_time = time.time()
    game = Game(heuristic_method)
    game.find_solution()
    end_time = time.time()

    ##Metrics
    total_runtime = end_time - start_time
    nr_of_boards = game.get_number_of_Boards()
    solution_complexity = game.get_complexity_of_solution()

    return {
        "Runtime": total_runtime,
        "Number of Boards": nr_of_boards,
        "Complexity": solution_complexity
    }

def start_games(nr_of_games, heuristic_method):
    results = []
    threads = []

    lock = threading.Lock()
    def solved_thread(instance_id, heuristic_method):
        result = solve_puzzle(instance_id, heuristic_method)
        with lock:                  #ensure only one thread writes to results at a time
            results.append(result)

    ##Threading for each game
    for instance_id in range(1, nr_of_games + 1):
        thread = threading.Thread(target=solved_thread, args=(instance_id, heuristic_method))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


#########################################
def analyze_results(results):
    ##If more boards have the same complexity and board nr. they will be added together to get the average runtime
    complexity_sum = 0
    grouped_results = defaultdict(list)
    for result in results:
        complexity = result["Complexity"]
        grouped_results[complexity].append(result)

    ##Calculate average runtime for each complexity
    averages = []
    for complexity, games in grouped_results.items():
        avg_runtime = sum(game["Runtime"] for game in games) / len(games)
        avg_memory = sum(game["Number of Boards"] for game in games) / len(games)
        number_of_games = len(games)
        averages.append({
            "Complexity": complexity,
            "Average Runtime": avg_runtime,
            "Average Memory Usage": avg_memory,
            "Number of Games": number_of_games
        })

    averages.sort(key=lambda x: x["Complexity"])
    return averages

##Create complexity table
def print_results(result_h1, result_h2):


    ##Get complexity levels
    complexities = set([r["Complexity"] for r in result_h1] + [r["Complexity"] for r in result_h2])
    ##Sort complexity levels
    complexities = sorted(complexities)

    # Print header
    print(f"{'Complexity':<15}{'H1 Avg Runtime':<20}{'H2 Avg Runtime':<20}{'H1 Avg Memory':<20}{'H2 Avg Memory':<20}")
    print("-" * 95)

    ##Create the comparison table

    ##Print the table
    for complexity in complexities:
        h1_result = next((r for r in result_h1 if r["Complexity"] == complexity), None)
        h2_result = next((r for r in result_h2 if r["Complexity"] == complexity), None)

        # Extract runtime values, or use "N/A" if not available
        h1_runtime = f"{h1_result['Average Runtime']:.5f}" if h1_result else "N/A"
        h2_runtime = f"{h2_result['Average Runtime']:.5f}" if h2_result else "N/A"
        h1_memory = f"{h1_result['Average Memory Usage']:.2f}" if h1_result else "N/A"
        h2_memory = f"{h2_result['Average Memory Usage']:.2f}" if h2_result else "N/A"

        print(f"{complexity:<15}{h1_runtime:<20}{h2_runtime:<20}{h1_memory:<20}{h2_memory:<20}")



##Start games
result_h1 = start_games(nr_of_games, "h1")
result_h2 = start_games(nr_of_games, "h2")

##Analyze results
average_h1 = analyze_results(result_h1)
average_h2 = analyze_results(result_h2)

print_results(average_h1, average_h2)

print(f"Total puzzles processed: {len(result_h1)} for H1, {len(result_h2)} for H2")

#result = solve_puzzle(2, "h2")
#print(f"Complexity: {result['Complexity']}")

##print(average_h1, average_h2)


##TODO split into different complexities








