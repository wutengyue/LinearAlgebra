import numpy as np

if __name__ == '__main__':
    print(np.__version__)

    lst = [1, 2, 3]
    vec = np.array(lst)
    print(type(vec))
    print(vec)
    print('-' * 10)

    # 一维
    print(np.zeros(5))
    print(np.shape(np.zeros(5)))
    print('-' * 10)

    # 二维, 3个1维的向量
    print(np.zeros([3, 2]))
    print(np.shape(np.zeros([3, 2])))
    print('-' * 10)

    # 三维, 3个2维的向量
    print(np.zeros([3, 2, 2]))
    print('-' * 10)

    # np.array的创建
    print(np.zeros(5, ))
    print(np.ones(5, ))
    print(np.full(5, 6.))
    print(np.full((5, 1), 6.))
    print('-' * 10)

    # np.array基本属性
    print(vec)
    print(vec.size)
    print(len(vec))
    print(vec[0])
    print(vec[0:1])
    print(type(vec[0:1]))
    print('-' * 10)

    # np.array基本运算
    vec2 = np.array([4, 5, 6])
    print(vec + vec2)
    print(vec - vec2)
    print(2 * vec)
    print(vec.dot(vec2))

    print(np.linalg.norm(vec))
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))
