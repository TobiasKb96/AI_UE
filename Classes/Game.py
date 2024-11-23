import numpy as np
from networkx.algorithms.shortest_paths.generic import shortest_path

from Classes.Board import Board


#aka Tree

class Game:
    def __init__(self, width, height):
        self.board_states = None
        self.width = width
        self.height = height
        self.root_board : Board = Board()
        self.list_of_boards = []


    def we_need_to_deeper(self,parent_board: Board = None):

        if parent_board is None:
            self.root_board.initBoard(self.width, self.height)
            self.root_board.printBoard()
            self.list_of_boards.append(self.root_board)
            self.root_board.h2()
            self.root_board.update_cost()
            self.board_states = {tuple(self.root_board.array.flatten())}
            return self.root_board

        moves_list = parent_board.posible_moves()

        for element in moves_list:
            child_board = Board(parent_board)
            child_board.swtich_x_and_0(element)
            child_board.h2()
            child_board.update_cost()

            board_state = tuple(child_board.array.flatten())
            if board_state not in self.board_states:
                self.list_of_boards.append(child_board)
                parent_board.children.append(child_board)
                self.board_states.add(board_state)  # Add new state to the set

                if np.array_equal(child_board.array, child_board.goal):
                    print("Solution Found!")
                    self.print_shortest_path(child_board)
                    return

        self.list_of_boards.remove(parent_board)
        self.list_of_boards.sort(key = lambda board: board.overall_cost)


    def print_shortest_path(self, solution_board: Board):
        path = []
        current_board = solution_board

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






