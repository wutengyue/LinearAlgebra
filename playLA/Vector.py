import copy


class Vector:
    def __init__(self, lst):
        """传入一个数组"""
        self._values = copy.deepcopy(lst)  # deep copy传值, 不影响原list

    # def __iter__(self):
    #     """返回向量的迭代器"""
    #     return self._values.__iter__()

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self) == len(other), "Error in adding. Length of vectors must be same."

        return Vector([a + b for a, b in zip(self, other)])

    def __str__(self):
        """
        print该变量时，输出到屏幕上的内容
        :return: ex: Vector(1, 3)
        """
        return 'Vector({})'.format(', '.join(str(i) for i in self._values))

    def __len__(self):
        return len(self._values)

    # def __getitem__(self, index):
    #     return self._values[index]

    __repr__ = __str__
