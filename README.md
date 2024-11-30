Modules

    Board.py: Defines the Board class for managing board states, heuristic calculations, and transitions.
    Game.py: Contains the Game class, which organizes A* search execution and maintains the solution path.
    UE1_main.py: Main script for initialization, execution, and result display.

Classes
Board (Board.py)

    Represents a single board state.

    Attributes:
        array: Current board configuration.
        goal: Target configuration.
        heuristic_estimate: Value based on the heuristic method.
        cost: Steps taken to reach the state.
        overall_cost: Combined cost (A* function value f(n)).
        children: List of valid child states.
        parent: Pointer to the previous board state.

    Key Methods:
        initBoard: Initializes a random solvable board.
        is_solvable: Verifies solvability of the board.
        h1: Computes Hamming distance.
        h2: Computes Manhattan distance.
        possible_moves: Identifies tiles that can be swapped with the blank.
        update_cost: Updates the overall cost for the board state.

Game (Game.py)

    Manages the search process for a solution.

    Attributes:
        root_board: Starting board state.
        solution_board: Final solved board state.
        list_of_boards: Open list of states for exploration.
        heuristic_method: Chosen heuristic ("h1" or "h2").

    Key Methods:
        explore_child_boards: Expands child states from a parent.
        find_solution: Executes the A* search algorithm.
        print_shortest_path: Displays the path from the initial to the solved state.

Fundamental Design Decisions

    Heuristics: The choice of Manhattan and Hamming distance ensures admissibility and optimality.

    Data Structures: 
        numpy arrays for efficient board operations.
        Sets to track explored states, avoiding redundancy.

    Class Hierarchy:
        Separation of Board and Game ensures modularity and scalability.

    Algorithm Efficiency:
        Priority queue-like behavior using sorted lists optimizes A* state selection.

Discussion and Conclusions

    Experimental Observations:
        Manhattan heuristic performs better for deeper solutions due to finer granularity.
        Memory usage scales with problem depth.

    Complexity Comparison:
        Manhattan is computationally more expensive but reduces total explored states.

    Alternatives and Improvements:
        Implementing a true priority queue using heapq for better efficiency.
        Parallelized exploration of multiple games.

Fundamental Concepts and Algorithm Recall A* Algorithm

    Definition: A* combines the actual cost to reach a node (g(n)) with an estimated cost to the goal (h(n)).
        f(n) = g(n) + h(n)

    Steps:
        Initialize open and closed lists.
        Expand the node with the smallest f(n).
        Generate children, calculate their costs, and add unexplored states to the open list.
        Repeat until the goal is reached or no states remain.

Fundamental Concepts

    Admissible Heuristics: Ensure that the heuristic never overestimates the cost to the goal.
    Search Trees: Represent states and transitions as nodes and edges.
    Priority Queues: Manage the open list efficiently.

Derived Data Structures, Methods, and Variables
Data Structures

    Board:
        2D numpy array.
        Attributes for tracking cost, parent, and children.
    Game:
        List of Board objects for managing states.
        Set for tracking explored states.

Methods

    Board Initialization: Ensures solvability using inversion count.
    Heuristic Functions:
        h1: Counts misplaced tiles.
        h2: Sums Manhattan distances.
    State Exploration:
        possible_moves: Generates valid moves for the blank tile.

Design and Implementation

    Design:
        Modular structure separating game logic (Game) from state logic (Board).
        Encapsulation of heuristics within the Board class.

    Testing:
        Unit tests for board initialization and heuristic calculations.
        Performance tests for multiple random states.

    Documentation:
        Inline comments for methods and variables.
        Detailed output for solution paths.
