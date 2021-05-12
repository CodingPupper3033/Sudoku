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

        # Find numbers we have
        list_numbs_have = []
        for square in self.squares_filled:
            list_numbs_have.append(square.numb_show)

        # Remove all possible occurrences of these numbers
        for square in self.squares_empty:
            for numb_cant_be in list_numbs_have:
                square.cant_be_numb(numb_cant_be)
