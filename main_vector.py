from playLA.Vector import Vector
from collections.abc import Iterable, Iterator


if __name__ == '__main__':
    vector = Vector([1, 2, 3])
    # vector = Vector(1)
    # print(vector)
    # print(isinstance(vector, Iterable))
    # print(isinstance(vector, Iterator))
    # for i in vector:
    #     print(i)
    # print(dir(vector))
    # exit()
    # print(len(vector))
    # print(vector[0])
    # print('-'*10)
    v1 = Vector([1, 1])
    # print(id(v1))
    # print(v1 + Vector([2, 2]))
    # print(v1 - Vector([2, 2]))
    # print(v1 * 3)
    # print(3 * v1)
    # print(+v1)
    # print(-v1)
    # exit()

    zero2 = Vector.zero(2)
    print(zero2)
    print(v1 + zero2)
