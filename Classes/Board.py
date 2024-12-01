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
        # Count inversions
        inversions = 0
        for i in range(len(sequence)):
            for j in range(i + 1, len(sequence)):
                if sequence[i] > sequence[j] and sequence[j] != 0:
                    inversions += 1

        # A 3x3 puzzle is solvable if inversions are even
        return inversions % 2 == 0

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
        # Iterate through the board to calculate the distance for each tile
        distance = 0
        for i in range(self.width):
            for j in range(self.height):
                value = self.array[i][j]
                if value != 0:  # Ignore the blank tile
                    goal_position = np.argwhere(self.goal == value)[0]
                    distance += abs(goal_position[0] - i) + abs(goal_position[1] - j)
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




