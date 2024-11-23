import random
import numpy as np

class GameBoard:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = np.zeros((self.height,self.width), dtype=int)
        #self.printBoard()
        self.initBoard()


    def initBoard(self):
        allNumbers = list(range(self.width * self.height))
        random.shuffle(allNumbers)
        k = 0
        #print(allNumbers)
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j] = allNumbers[k]
                k += 1


    def printBoard(self):
        for row in self.board:
            print(row)

