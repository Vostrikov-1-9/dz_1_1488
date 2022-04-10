from app.matrix import Matrix


class Matrix3x3(Matrix):
    def __init__(self, spisok=None):
        if spisok is None:
            spisok = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        super().__init__(spisok)
        if not self._is_valid():
            raise ValueError("Only matrix 3x3")

    def input(self):
        super().input()
        if not self._is_valid():
            raise ValueError("Only matrix 3x3")

    def _is_valid(self) -> bool:
        if len(self.spisok) != 3:
            return False
        elif len(self.spisok[0]) != 3:
            return False
        elif len(self.spisok[1]) != 3:
            return False
        elif len(self.spisok[2]) != 3:
            return False
        return True

    def determinant(self):
        pos_on = self.spisok[0][0] * self.spisok[1][1] * self.spisok[2][2]
        pos_tw = self.spisok[0][1] * self.spisok[1][2] * self.spisok[2][0]
        pos_th = self.spisok[2][1] * self.spisok[1][0] * self.spisok[0][2]
        min_pos_on = self.spisok[0][2] * self.spisok[1][1] * self.spisok[2][0]
        min_pos_tw = self.spisok[0][1] * self.spisok[1][0] * self.spisok[2][2]
        min_pos_th = self.spisok[1][2] * self.spisok[2][1] * self.spisok[0][0]
        return pos_on + pos_tw + pos_th - min_pos_on - min_pos_tw - min_pos_th


m = Matrix3x3([[1, 2, 3], [4, 5, 6], [10, 12, 13]])
assert m.determinant() == 3
