import numpy as np
from networkx.algorithms.operators.binary import difference


class GameBoard:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.size = width*height
        self.board = np.zeros((self.width,self.height), dtype=int)
        #self.printBoard()
        self.goal = np.arange(0, self.size).reshape(width, height)
        self.initBoard()

    def initBoard(self):
        allNumbers = list(range(self.size))
        np.random.shuffle(allNumbers)
        k = 0
        #print(allNumbers)

        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j] = allNumbers[k]
                k += 1


    def printBoard(self):
        for row in self.board:
            print(row)

    def  h1(self):
        differences = np.sum(self.board != self.goal)
        print(differences)
        return differences

    def h2(self):
        # Initialize the Manhattan distance sum
        distance = 0

        # Iterate through the board to calculate the distance for each tile
        goal_value = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] != self.goal[i][j]:
                    board_coordinates = np.argwhere(self.board == goal_value)[0]
                    print(board_coordinates)
                    goal_value += 1
                    distance += abs((board_coordinates[0]) - i) + abs((board_coordinates[1]) - j)

        print(distance)
        return distance






