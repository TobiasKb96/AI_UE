import numpy as np
from networkx.algorithms.operators.binary import difference

#aka Node

class Board:

    def __init__(self,parent_board=None):
        if parent_board is None:
            self.array = None
            self.goal = None
            self.children = []
            self.cost = 0
            self.heuristic_estimate = 0
            self.overall_cost = 0
            self.parent = None


        else:

            self.width = parent_board.width
            self.height = parent_board.height
            self.size = parent_board.size
            self.array = np.copy(parent_board.array)
            self.goal = parent_board.goal
            self.cost = parent_board.cost
            self.children = []
            self.heuristic_estimate = parent_board.heuristic_estimate
            self.overall_cost = parent_board.overall_cost
            self.parent = parent_board

    def is_solvable(self, sequence):
        # Filter out the blank tile (0)
        sequence_no_zero = [tile for tile in sequence if tile != 0]

        # Count inversions
        inversions = 0
        for i in range(len(sequence_no_zero)):
            for j in range(i + 1, len(sequence_no_zero)):
                if sequence_no_zero[i] > sequence_no_zero[j]:
                    inversions += 1

        # Find the row of the blank tile (0) in the 2D representation
        zero_index = sequence.index(0)  # Position of the blank tile in the 1D sequence
        zero_row = zero_index // self.width  # Row of the blank tile in the 2D grid

        # Calculate the blank tile's row from the bottom
        blank_row_from_bottom = self.height - zero_row

        # Determine solvability based on grid width
        if self.width % 2 != 0:  # Odd-width grids
            return inversions % 2 == 0
        else:  # Even-width grids
            return (inversions + blank_row_from_bottom) % 2 == 0

    def initBoard(self, width, height):
            self.width = width
            self.height = height
            self.size = width * height
            self.array = np.empty((self.width, self.height), dtype=int)
            self.goal = np.arange(0, self.size).reshape(width, height)

            allNumbers = list(range(self.size))

            while(1):
                np.random.shuffle(allNumbers)
                if (self.is_solvable(allNumbers)):
                    break


            k = 0
            for i in range(self.width):
                for j in range(self.height):
                    self.array[i][j] = allNumbers[k]
                    k += 1


    def printBoard(self):
        for row in self.array:
            print(row)

    def  h1(self):
        differences = np.sum(self.array != self.goal)
        self.heuristic_estimate = differences

    def h2(self):
        # Initialize the Manhattan distance sum
        distance = 0

        # Iterate through the board to calculate the distance for each tile
        goal_value = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.array[i][j] != self.goal[i][j]:
                    board_coordinates = np.argwhere(self.array == goal_value)[0]
                    goal_value += 1
                    distance += abs((board_coordinates[0]) - i) + abs((board_coordinates[1]) - j)
        self.heuristic_estimate = distance

    def swtich_x_and_0(self,x):
        pos1 = tuple(np.argwhere(self.array == 0)[0])  # Get position of 0
        pos2 = tuple(np.argwhere(self.array == x)[0])  # Get position of x

        # Swap the numbers
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
        self.cost += 1

    def posible_moves(self):
        zero_position = tuple(np.argwhere(self.array == 0)[0])
        row, col = zero_position
        neighbors = []

        if row > 0:  # Up
            neighbors.append(self.array[row - 1, col])
        if row < self.array.shape[0] - 1:  # Down
            neighbors.append(self.array[row + 1, col])
        if col > 0:  # Left
            neighbors.append(self.array[row, col - 1])
        if col < self.array.shape[1] - 1:  # Right
            neighbors.append(self.array[row, col + 1])

        return neighbors

    def update_cost(self):
        self.overall_cost = self.cost + self.heuristic_estimate






