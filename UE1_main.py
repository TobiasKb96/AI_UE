import numpy as np

from Classes.Board import Board
from Classes.Game import Game

newGame = Game(3,3)
newGame.we_need_to_deeper()

newGame.we_need_to_deeper(newGame.list_of_boards[0])
newGame.we_need_to_deeper(newGame.list_of_boards[0])

while newGame.list_of_boards:
    # Process the board with the lowest cost
    current_board = newGame.list_of_boards[0]
    newGame.we_need_to_deeper(current_board)

    # Break if the solution is found (handled inside `we_need_to_deeper`)
    if np.array_equal(current_board.array, current_board.goal):
        break


#board = Board()
#board.initBoard(3,3)
#board.printBoard()
#print(board.posible_moves())
# board.h1()
# board.h2()
# board2 = Board(board)
#
# print(board2.posible_moves())
# board2.printBoard()
