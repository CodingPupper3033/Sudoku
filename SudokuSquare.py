class SudokuSquare:
    def __init__(self, numb_show=0, numbs_can_be=None):
        if numbs_can_be is None and numb_show == 0:
            self.numbs_can_be = list(range(1, 10))
        else:
            self.set_square_numb(numb_show)
        self.update_numb_show()

    def cant_be_numb(self, *numbs):
        for numb in numbs:
            if numb in self.numbs_can_be:
                self.numbs_can_be.remove(numb)
        self.update_numb_show()

    def set_square_numb(self, numb):
        self.numbs_can_be = [numb]
        self.update_numb_show()

    def update_numb_show(self):
        if self.showing_numb():
            self.numb_show = self.numbs_can_be[0]
        if len(self.numbs_can_be) == 0:
            raise RuntimeError("No numbers left to be")

    def showing_numb(self):
        return len(self.numbs_can_be) == 1

    def get_square_save(self):
        can_be_boolean = []
        for numb in range(0,10):
            can_be_boolean.append(numb in self.numbs_can_be)
        return can_be_boolean

    def same_square(self, square_save):
        square_save_this = self.get_square_save()

        return square_save == square_save_this

    def __str__(self):
        if self.numb_show != 0:
            return str(self.numb_show)
        else:
            return " "
