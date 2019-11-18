class Vector:
    def __init__(self, lst):
        """传入一个数组"""
        self._values = lst

    def __str__(self):
        """
        print该变量时，输出到屏幕上的内容
        :return: ex: Vector(1, 3)
        """
        return 'Vector({})'.format(', '.join(str(i) for i in self._values))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    __repr__ = __str__
