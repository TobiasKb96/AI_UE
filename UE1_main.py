##TODO multithreaded 100 Games
##TODO console output ask for solved board
##TODO table with complexity comparisons of different heuristics
##TODO comment code -> Julian
##TODO rework documentation ->Julian
import concurrent
import threading
import time
import concurrent.futures

from Classes.Game import Game






###############################


#####Test
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
        total_runtime,
        nr_of_boards,
        solution_complexity
    }

def start_games(nr_of_games, heuristic_method):
    results = []
    threads = []

    def solved_thread(instance_id, heuristic_method):
        result = solve_puzzle(1, heuristic_method)
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
    for result in results:
        complexity = result
        if complexity not in complexity_sum:
            complexity_sum[complexity] = []
        complexity_sum[complexity].append(result)

    ##Calculate average runtime for each complexity
    averages = []
    for complexity, runtimes in complexity_sum.items():
        avg_runtime = sum(r["Runtime"] for r in runtimes) / len(runtimes)
        number_of_games = len(runtimes)
        averages.append({
            "Complexity": complexity,
            "Average Runtime": avg_runtime,
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

    ##Create the comparison table

    ##Print the table


##Start games
result_h1 = start_games(nr_of_games, "h1")
result_h2 = start_games(nr_of_games, "h2")

##Analyze results
average_h1 = analyze_results(result_h1)
average_h2 = analyze_results(result_h2)

print(average_h1, average_h2)


##TODO split into different complexities








