import numpy as np

from Classes.Board import Board


# Managing A* search execution and maintains the solution path

class Game:
    # Input: A string specifying the heuristic method (h1 for Hamming, h2 for Manhattan)
    # Output: Initialized Game object
    def __init__(self, heuristic_method):
        self.heuristic_method = heuristic_method
        self.board_states = set()
        self.root_board : Board = Board()
        self.list_of_boards = []
        self.solution_board : Board = None

    # Input: Parent board (if present)
    # Output: All valid child boards and an updated game state
    # Function:     Initializes the root board if parent_board is None
    #               Generate all valid child boards
    #               Ensures each state is unique
    def explore_child_boards(self, parent_board: Board = None):

        if parent_board is None:
            self.root_board.initBoard()
            self.list_of_boards.append(self.root_board)

            if self.heuristic_method == "h1":
                self.root_board.h1()
            elif self.heuristic_method == "h2":
                self.root_board.h2()
            else:
                print("Heuristic method not recognized")

            self.root_board.update_cost()
            self.board_states = {tuple(self.root_board.array.flatten())}
            return self.root_board

        else:

            moves_list = parent_board.possible_moves()
            for element in moves_list:
                child_board = Board(parent_board)
                child_board.switch_x_and_0(element)

                if (self.heuristic_method == "h1"):
                    child_board.h1()
                elif (self.heuristic_method == "h2"):
                    child_board.h2()
                else:
                    print("Heuristic method not recognized")

                child_board.update_cost()

                board_state = tuple(child_board.array.flatten())

                if board_state not in self.board_states:
                    self.list_of_boards.append(child_board)
                    parent_board.children.append(child_board)
                    self.board_states.add(board_state)  # Add new state to the set

    # Output: Prints the sequence of moves from the root board to the solution
    # Function: Backtracks from the solution board to the root, collecting and printing each step
    def print_shortest_path(self):
        path = []
        current_board = self.solution_board

        # Backtrace to the root board
        while current_board is not None:
            path.append(current_board)
            current_board = current_board.parent

        # Reverse the path to go from root to solution
        path.reverse()

        # Print the path
        print("Shortest Path to Solution:")
        for step, board in enumerate(path):
            print(f"Step {step}:")
            board.printBoard()
            print()

    # Output: Determines the optimal solution board
    # Function: Implements the A* algorithm
    #           Sorts unexplored boards by their costs
    #           Stops when the goal state is found
    def find_solution(self):
        # Initialize -> create root board
        self.explore_child_boards()

        # Continue until all boards are explored or the solution is confirmed optimal
        while 1:

            self.list_of_boards.sort(key=lambda board: board.overall_cost)

            # Process the board with the lowest cost (sorted by f(n))
            current_board = self.list_of_boards.pop(0)  # Remove the board with the smallest f(n)

            # If the current board is the goal, stop
            if np.array_equal(current_board.array, current_board.goal):
                self.solution_board = current_board
                break

            # Otherwise, explore child boards
            self.explore_child_boards(current_board)

    # Output: The number of unique board states explored
    # Function: Returns the size of the board_states set
    def get_number_of_Boards(self):
        return len(self.board_states)

    # Output: The depth of the solution
    # Function: Counts the number of boards traversed in the shortest solution path
    def get_complexity_of_solution(self):
        complexity = 0
        current_board = self.solution_board

        while current_board is not None:
            current_board = current_board.parent
            complexity += 1

        return complexity - 1



