from playLA.Vector import Vector
from collections.abc import Iterable, Iterator


if __name__ == '__main__':
    vector = Vector([1, 2, 3])

    # # 迭代
    # print('Iterable,', isinstance(vector, Iterable))
    # print('Iterator,', isinstance(vector, Iterator))
    # for i in vector:
    #     print('i,', i)
    # print('sum,', sum(vector))
    
    # # 魔法方法
    # print(len(vector))
    # print(vector[0])
    # print('-'*10)

    # # 向量基本运算
    # print(vector + Vector([1, 1, 1]))
    # print(vector - Vector([1, 1, 1]))
    # print(vector * 3)
    # print(3 * vector)
    # print(+vector)
    # print(-vector)

    # # 零向量
    # zero2 = Vector.zero(dim=3)  # 二维零向量
    # print(zero2)
    # print(vector + zero2)

    # # 向量的模
    # print(Vector([3, 4]).norm())
    # print(vector.norm())

    # # 单位向量
    # print(vector.normalize())
    # print(vector.normalize().norm())
    # try:
    #     print(Vector.zero(2).normalize())
    # except ZeroDivisionError as e:
    #     print('Error:', e)

    # 向量点乘
    print(vector.dot(vector))
    print(vector.dot(Vector([1, 2])))
