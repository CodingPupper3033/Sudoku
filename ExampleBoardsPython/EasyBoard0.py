from SudokuBoard import SudokuBoard

board = SudokuBoard()
board.square_is([0, 1], 3)
board.square_is([0, 4], 1)
board.square_is([0, 7], 6)

board.square_is([1, 0], 7)
board.square_is([1, 1], 5)
board.square_is([1, 4], 3)
board.square_is([1, 7], 4)
board.square_is([1, 8], 8)

board.square_is([2, 2], 6)
board.square_is([2, 3], 9)
board.square_is([2, 4], 8)
board.square_is([2, 5], 4)
board.square_is([2, 6], 3)

board.square_is([3, 2], 3)
board.square_is([3, 6], 8)

board.square_is([4, 0], 9)
board.square_is([4, 1], 1)
board.square_is([4, 2], 2)
board.square_is([4, 6], 6)
board.square_is([4, 7], 7)
board.square_is([4, 8], 4)

board.square_is([5, 2], 4)
board.square_is([5, 6], 5)

board.square_is([6, 2], 1)
board.square_is([6, 3], 6)
board.square_is([6, 4], 7)
board.square_is([6, 5], 5)
board.square_is([6, 6], 2)

board.square_is([7, 0], 6)
board.square_is([7, 1], 8)
board.square_is([7, 4], 9)
board.square_is([7, 7], 1)
board.square_is([7, 8], 5)

board.square_is([8, 1], 9)
board.square_is([8, 4], 4)
board.square_is([8, 7], 3)