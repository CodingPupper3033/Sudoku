from ExampleBoardsPython import EasyBoard0
from MakeBoardFromFile import MakeBoardFromFile
from SudokuBoard import SudokuBoard
from SudokuStrand import SudokuStrand

'''
board = SudokuBoard(9)
board.square_is([0, 0], 1)
board.square_is([0, 1], 2)
board.square_is([0, 2], 3)
board.square_is([0, 3], 4)
board.square_is([0, 4], 5)
board.square_is([0, 5], 6)
board.square_is([0, 6], 7)
board.square_is([0, 7], 8)
'''

max_runs = 10000

board = EasyBoard0.board



# board.square_is([])

pos_on = [0, 0]


def run_once():
    # Row Solve
    row_array = board.get_row(pos_on[0])
    row_strand = SudokuStrand(row_array)
    row_strand.try_run()

    # Column Solve
    col_array = board.get_column(pos_on[1])
    col_strand = SudokuStrand(col_array)
    col_strand.try_run()

    # Box Solve
    box_array = board.get_box(pos_on)
    box_strand = SudokuStrand(box_array)
    box_strand.try_run()

    move_next_pos()


def move_next_pos():
    # Move Forwards one
    pos_on[1] = pos_on[1] + 1
    if pos_on[1] == 9:
        pos_on[1] = 0
        pos_on[0] += 1
    if pos_on[0] == 9:
        pos_on[0] = 0


count = 0
print("Original:")
print(board)
print("")
print("")
print("")
while count < max_runs and not board.is_filled():
    run_once()
    count += 1
print("Solved in",count,"steps:")
print(board)
