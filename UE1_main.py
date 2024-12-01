import threading
import time
from Classes.Game import Game

nr_of_games = 10


def solve_puzzle(instance_id, heuristic_method="h1"):
    ## Measure runtime
    start_time = time.time()
    game = Game(heuristic_method)
    game.find_solution()
    end_time = time.time()

    ## Metrics
    total_runtime = end_time - start_time
    nr_of_boards = game.get_number_of_Boards()
    solution_complexity = game.get_complexity_of_solution()

    return {
        "Instance ID": instance_id,
        "Runtime": total_runtime,
        "Boards Checked": nr_of_boards,
        "Complexity": solution_complexity,
    }


##### Start Games with Multithreading
def start_games(nr_of_games, heuristic_method):
    results = []
    threads = []

    def solved_thread(instance_id, heuristic_method):
        result = solve_puzzle(instance_id, heuristic_method)
        results.append(result)

    ## Create threads for each game
    for instance_id in range(1, nr_of_games + 1):
        thread = threading.Thread(target=solved_thread, args=(instance_id, heuristic_method))
        threads.append(thread)
        thread.start()

    ## Wait for all threads to finish
    for thread in threads:
        thread.join()

    return results


##### Analyze Results
def analyze_results(results):
    complexity_groups = {}

    ## Group by complexity only
    for result in results:
        complexity = result["Complexity"]
        if complexity not in complexity_groups:
            complexity_groups[complexity] = []
        complexity_groups[complexity].append(result["Runtime"])

    ## Calculate averages per complexity
    averages = []
    for complexity, runtimes in complexity_groups.items():
        avg_runtime = sum(runtimes) / len(runtimes)
        num_games = len(runtimes)
        averages.append({
            "Complexity": complexity,
            "Average Runtime": avg_runtime,
            "Number of Games": num_games,
        })

    ## Sort averages by complexity
    averages.sort(key=lambda x: x["Complexity"])

    return averages


##### Print Results
def print_results(results_h1, results_h2):
    ## Extract unique complexities
    complexities = set([r["Complexity"] for r in results_h1] + [r["Complexity"] for r in results_h2])
    complexities = sorted(complexities)

    ## Print header
    print(f"{'Complexity':<12} | {'H1 Avg Runtime':<15} | {'H1 Games':<10} | {'H2 Avg Runtime':<15} | {'H2 Games':<10}")
    print("-" * 70)

    ## Iterate over complexities
    for complexity in complexities:
        h1_data = next((r for r in results_h1 if r["Complexity"] == complexity), None)
        h2_data = next((r for r in results_h2 if r["Complexity"] == complexity), None)

        h1_runtime = f"{h1_data['Average Runtime']:.2f}" if h1_data else "N/A"
        h1_games = h1_data["Number of Games"] if h1_data else "N/A"
        h2_runtime = f"{h2_data['Average Runtime']:.2f}" if h2_data else "N/A"
        h2_games = h2_data["Number of Games"] if h2_data else "N/A"

        ## Print row
        print(f"{complexity:<12} | {h1_runtime:<15} | {h1_games:<10} | {h2_runtime:<15} | {h2_games:<10}")


##### Main Execution
if __name__ == "__main__":
    ## Run games for both heuristics
    results_h1 = start_games(nr_of_games, "h1")
    results_h2 = start_games(nr_of_games, "h2")

    ## Analyze results
    average_h1 = analyze_results(results_h1)
    average_h2 = analyze_results(results_h2)

    ## Print results
    print_results(average_h1, average_h2)
