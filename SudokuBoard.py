from SudokuSquare import SudokuSquare


class SudokuBoard:
    def __init__(self, size=9):
        self.size = size
        board = []

        for rowN in range(size):
            row = []
            for colN in range(size):
                square = SudokuSquare()
                row.append(square)
            board.append(row)
        self.board = board

    def square_cant_be(self, pos, *numbs):
        square = self.board[pos[0]][pos[1]]
        for numb in numbs:
            square.cant_be_numb(numb)

    def square_is(self, pos, numb):
        square = self.board[pos[0]][pos[1]]
        square.set_square_numb(numb)

    def get_row(self, index):
        return self.board[index]

    def get_column(self, index):
        out = []
        for row in self.board:
            out.append(row[index])
        return out

    def get_box(self, pos):
        temp_pos = [0, 0]
        temp_pos[0] = pos[0] // 3
        temp_pos[1] = pos[1] // 3
        out = []
        for rowN in range(temp_pos[0] * 3, temp_pos[0] * 3 + 3):
            for colN in range(temp_pos[1] * 3, temp_pos[1] * 3 + 3):
                out.append(self.board[rowN][colN])
        return out

    def is_filled(self):
        for row in self.board:
            for square in row:
                if not (square.showing_numb()):
                    return False
        return True

    def __str__(self):
        out = ""
        for squareRow in self.board:
            temp = ""
            for square in squareRow:
                temp += str(square) + " ┃ "
            temp = temp[0:len(temp) - 3]
            out += temp + "\n"
            temp_middle = "━━━╋" * (len(temp) // 4 + 1)
            temp_middle = temp_middle[1:len(temp_middle) - 2]
            out += temp_middle
            out += "\n"
        out = out[0:len(out) - len(temp_middle) - 2]
        return out
