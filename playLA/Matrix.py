from playLA.Vector import Vector


class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls, row_num, col_num):
        """返回一个row_num行，col_num列的零矩阵"""
        return Matrix([[0] * col_num] for i in range(row_num))

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

    def __add__(self, another):
        """返回两个矩阵的加法结果"""
        assert self.shape() == another.shape(), 'Error in adding. Shape of matrix must be same.'
        return Matrix([
            [a + b for a, b in zip(self.row_vector(i), another.row_vector(i))] for i in range(self.row_num())
        ])

    def __sub__(self, another):
        """返回两个矩阵的减法结果"""
        assert self.shape() == another.shape(), 'Error in subtracting. Shape of matrix must be same.'
        return Matrix([
            [a - b for a, b in zip(self.row_vector(i), another.row_vector(i))] for i in range(self.row_num())
        ])

    def __mul__(self, k):
        """返回矩阵数量乘结果，矩阵在左"""
        return Matrix([
            [e * k for e in self.row_vector(i)] for i in range(self.row_num())
        ])

    def __rmul__(self, k):
        """返回矩阵的数量乘结果，矩阵在右"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果矩阵"""
        return self * (1/k)
    
    def __pos__(self):
        """返回矩阵取正的结果"""
        return self * 1

    def __neg__(self):
        """返回矩阵取负的结果"""
        return self * -1

    def dot(self, another):
        """返回矩阵乘法的结果"""
        if isinstance(another, Vector):
            assert self.col_num() == len(another), "Error in Matrix-Vector Multiplication, the col num of Matrix and the length of Vector must be same."
            # return Vector([
                # sum([a * b for a, b in zip(self.row_vector(i), another)]) for i in range(self.row_num())
            # ])

            return Vector([
                self.row_vector(i).dot(another) for i in range(self.row_num())
            ])

if __name__ == '__main__':
    matrix = Matrix([[1, 2, 3], [4, 5, 6]])
    print('matrix', matrix)
    # print(matrix.size())
    # print(matrix.shape())
    # print(len(matrix))
    # print(matrix[0, 0])
    # print(matrix * 2)
    # print(3 * matrix)
    # print(matrix / 2)
    # print(+matrix)
    # print(-matrix)

    # matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
    # print('matrix2', matrix2)
    # print('add', matrix + matrix2)
    # print('sub', matrix - matrix2)

    # print(Matrix.zero(3,4))

    vector = Vector([1, 2, 3])
    print(matrix.dot(vector))
