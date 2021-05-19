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

        # ---

        # Set number if it is the only one in it
        for numb in range(1,10):
            found_amount = 0
            recent_occurrence = None

            for square in self.squares_empty:
                if numb in square.numbs_can_be:
                    found_amount += 1
                    recent_occurrence = square

            if found_amount == 1:
                recent_occurrence.set_square_numb(numb)