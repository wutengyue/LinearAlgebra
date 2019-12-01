import numpy as np

if __name__ == '__main__':
    print(np.__version__)

    lst = [1, 2, 3]
    vec = np.array(lst)
    # print(type(vec))
    # print(vec)

    # print(np.zeros(5))
    # print(np.shape(np.zeros(5)))
    print('-' * 10)
    print(np.zeros([3, 2, 2]))
    print('-' * 10)
    print(np.zeros([2, 3, ]))
    print('-' * 10)
    print(np.zeros([3, 2, ]))
    print('-' * 10)
    # print(np.zeros([5, 2]))
