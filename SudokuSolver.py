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

max_runs = 1000


# board = MakeBoardFromFile("ExampleBoardsTXT\HardBoard0.txt").get_board()
board = MakeBoardFromFile("ExampleBoardsTXT\MediumBoard1.txt").get_board()
#board = EasyBoard0.board

# board.square_is([])

pos_on = [0, 0]


def solve_once(array_squares):
    strand = SudokuStrand(array_squares)
    strand.try_run()


def run_once():
    # Row Solve
    solve_once(board.get_row(pos_on[0]))

    # Column Solve
    solve_once(board.get_column(pos_on[1]))

    # Box Solve
    solve_once(board.get_box(pos_on))

    # Next Pos
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
max_do_nothings = 3
while count < max_runs and not board.is_filled():
    run_once()
    count += 1
if board.is_filled():
    print("Solved in", count, "steps:")
else:
    print("Unable to solve:")
print(board)
