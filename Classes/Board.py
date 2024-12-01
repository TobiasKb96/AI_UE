import numpy as np
#from networkx.algorithms.operators.binary import difference

#aka Node

class Board:

    def __init__(self,parent_board=None):
        self.width = 3
        self.height = 3
        self.size = 9
        self.children = []

        if parent_board is None:
            #initializes all variables
            self.array = np.empty((self.width, self.height), dtype=int)
            self.goal = None

            self.cost = 0
            self.heuristic_estimate = 0
            self.overall_cost = 0

            self.parent = None

        else:

            self.array = np.copy(parent_board.array)
            self.goal = parent_board.goal

            self.cost = parent_board.cost
            self.heuristic_estimate = parent_board.heuristic_estimate
            self.overall_cost = parent_board.overall_cost

            self.parent = parent_board

    def initBoard(self):

            ##Create Array as a goal from  0 to  8
            self.goal = np.arange(0, self.size).reshape(self.width, self.height)

     ##Generate random Board
            ##create list of numbers 0 to 8
            allNumbers = list(range(self.size)) ##012345678

            ##shuffles until solvable sequence is found
            while(1):
                np.random.shuffle(allNumbers) ##018274635
                if (self.is_solvable(allNumbers)):
                    break

            ##Force initial array
            #allNumbers = [1,2,0,3,4,5,6,7,8,9]

            ##fills array with solvable sequence
            k = 0
            for i in range(self.width):
                for j in range(self.height):
                    self.array[i][j] = allNumbers[k]
                    k += 1

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

    def printBoard(self):
        for row in self.array:
            print(row)

    ##Hamming heuristic
    def h1(self):
        differences = np.sum(self.array != self.goal)
        if differences > 0:
            differences  -= 1
        self.heuristic_estimate = differences
        #print(self.heuristic_estimate)

    ##Manhatten distance
    def h2(self):
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
        #print(self.heuristic_estimate)

    def switch_x_and_0(self, x):
        pos1 = tuple(np.argwhere(self.array == 0)[0])  # Get position of 0
        pos2 = tuple(np.argwhere(self.array == x)[0])  # Get position of x

        # Swap the numbers
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
        self.cost += 1

    def possible_moves(self):
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




