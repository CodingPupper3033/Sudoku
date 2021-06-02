from itertools import combinations

from SudokuSquare import SudokuSquare


class SudokuStrand:
    def __init__(self, sudoku_square_list):
        self.squares = sudoku_square_list
        self.squares_filled = []
        self.squares_empty = []

        self.set_lists_of_filled()

    def set_lists_of_filled(self):
        squares_filled = []
        squares_empty = []
        for square in self.squares:
            if square.showing_numb():
                squares_filled.append(square)
            else:
                squares_empty.append(square)
        self.squares_filled = squares_filled
        self.squares_empty = squares_empty

    def try_run(self):
        # Removal of one cell
        # Set filled lists
        self.set_lists_of_filled()

        # Find numbers we have showing
        list_numbs_have = []
        for square in self.squares_filled:
            list_numbs_have.append(square.numb_show)

        # Remove all possible occurrences of these shown numbers
        for square in self.squares_empty:
            for numb_cant_be in list_numbs_have:
                square.cant_be_numb(numb_cant_be)

        # Singleton
        # Set number if it is the only one in it
        for numb in range(1, 10):
            found_amount = 0
            recent_occurrence = None

            for square in self.squares_empty:
                if numb in square.numbs_can_be:
                    found_amount += 1
                    recent_occurrence = square

            if found_amount == 1:
                recent_occurrence.set_square_numb(numb)

        # ---
        # "Pair" Rule
        for numb in range(2,9):
            self.try_run_pair(numb)

    def try_run_pair(self, numb):
        self.set_lists_of_filled()
        combs = self.make_combinations(numb)

        for combo in combs:
            # Check if they are a pair

            if len(SudokuSquare.combine_possible_values(combo)) == numb:
                # Squares are a pair
                # Tell everyone else they are not these numbers
                for square_telling in self.squares_empty:
                    if not(square_telling in combo): # Not in the combo, can tell em
                        for numbToRemove in SudokuSquare.combine_possible_values(combo):
                            square_telling.cant_be_numb(numbToRemove)

    def make_combinations(self, length):
        comb = combinations(self.squares_empty, length)
        return list(comb)


if __name__ == "__main__":
    self = cells = [SudokuSquare(),
                    SudokuSquare(),
                    SudokuSquare()]
    cells[0].cant_be_numb(1, 2, 3, 4, 5, 6, 7)
    cells[2].cant_be_numb(1, 2, 3, 4, 5, 6, 7)
    sudokuStrand = SudokuStrand(cells)
    sudokuStrand.set_lists_of_filled()
    sudokuStrand.try_run()
