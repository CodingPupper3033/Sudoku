from SudokuSquare import SudokuSquare
from SudokuStrand import SudokuStrand

mode = "Strand"

if mode == "Square Blank":
    sudokuSquare = SudokuSquare()
    print(sudokuSquare.numbs_can_be)
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

