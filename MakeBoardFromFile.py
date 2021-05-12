from SudokuBoard import SudokuBoard


class MakeBoardFromFile:
    board = SudokuBoard()

    def __init__(self, name):
        self.file = open(name)

    def get_board(self):
        pos = [0, 0]
        for line in self.file:
            for char in line:
                if char.isnumeric():
                    numb = int(char)
                    self.board.square_is(pos, numb)
                pos[1] += 1
            pos[1] = 0
            pos[0] += 1
        return self.board
