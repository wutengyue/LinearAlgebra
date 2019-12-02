from playLA.Vector import Vector


class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def shape(self):
        """返回矩阵的形状: (行数，列数)"""
        return len(self._values), len(self._values[0])

    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    def row_vector(self, index):
        """返回矩阵第index行的行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵第index列的列向量"""
        return Vector(row[index] for row in self._values)

    def row_num(self):
        """返回矩阵行数"""
        return self.shape()[0]

    def col_num(self):
        """返回矩阵列数"""
        return self.shape()[1]

    __len__ = row_num

    def __getitem__(self, pos):
        """返回矩阵pos位置的某个元素"""
        r, c = pos
        return self._values[r][c]

    def __repr__(self):
        return 'Matrix({})'.format(self._values)

    __str__ = __repr__


if __name__ == '__main__':
    matrix = Matrix([[1, 2, 3], [4, 5, 6]])
    print(matrix)
    print(matrix.size())
    print(matrix.shape())
    print(len(matrix))
    print(matrix[0, 0])
