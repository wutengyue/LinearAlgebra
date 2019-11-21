import copy


class Vector:
    def __init__(self, lst):
        """传入一个数组"""
        self._values = copy.deepcopy(lst)  # deep copy传值, 不影响原list

    @classmethod
    def zero(cls, dim):
        """返回一个dim纬的零向量"""
        return Vector([0] * dim)

    def __iter__(self):
        """返回向量的迭代器，使向量可迭代，支持for循环"""
        return self._values.__iter__()

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self) == len(other), "Error in adding. Length of vectors must be same."

        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法，返回结果向量"""
        assert len(self) == len(other), "Error in adding. Length of vectors must be same."

        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """数量乘法，返回self * k, 返回结果向量"""
        return Vector([k * i for i in self])

    __rmul__ = __mul__
    """数量乘法，返回k * self, 返回结果向量"""

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __str__(self):
        """
        print该变量时，输出到屏幕上的内容
        :return: ex: Vector(1, 3)
        """
        return 'Vector({})'.format(', '.join(str(i) for i in self._values))

    __repr__ = __str__

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]
