from ExampleBoardsPython import EasyBoard0
from MakeBoardFromFile import MakeBoardFromFile
from SudokuSquare import SudokuSquare
from SudokuStrand import SudokuStrand

mode = "Combine Squares"

if mode == "Square Blank":
    sudokuSquare = SudokuSquare()
    sudokuSquare2 = SudokuSquare()
    sudokuSquare.set_square_numb(5)
    print(sudokuSquare2.numbs_can_be)
if mode == "Square Remove Numbs":
    sudokuSquare = SudokuSquare()
    sudokuSquare.cant_be_numb(1)
    print(sudokuSquare.numbs_can_be)
if mode == "Square Set Numb":
    sudokuSquare = SudokuSquare(5)
    print(sudokuSquare)
if mode == "Strand":
    cells = [SudokuSquare(),
             SudokuSquare(5),
             SudokuSquare()]
    sudokuStrand = SudokuStrand(cells)

    print("Squares Full:")
    for square in sudokuStrand.squares_filled:
        print("\t" + str(square))

    print("Squares Empty:")
    for square in sudokuStrand.squares_empty:
        print("\t" + str(square.numbs_can_be))
if mode == "Board":
    board = EasyBoard0.board
    print(board)
if mode == "Combine Squares":
    sudokuSquare = SudokuSquare()
    sudokuSquare.cant_be_numb(2,3,4,5,6)
    sudokuSquare2 = SudokuSquare()
    sudokuSquare2.set_square_numb(5)
    print(SudokuSquare.combine_possible_values([sudokuSquare,sudokuSquare2]))
