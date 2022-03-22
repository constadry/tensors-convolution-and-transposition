import numpy as np

def con():
    a = np.array([-1, 0, 0, -8, -3, 0, 1, 3, 7, 3, 1, 2, -4, 4, -2, 6])
    a = a.reshape([2, 2, 2, 2])
    s = np.einsum('ijji', a)
    print(s)

def trt():
    a = np.array([2, -1, -3, 8, -7, -6, -3, 4, 2, 2, 0, 5, 4, -1, -2, 4, 3, 7, 5, 3, -7, -1, 6, -3, 2, -4, 1])\
        .reshape((3, 3, 3))
    print(a)

    print('jik:')
    a1 = np.transpose(a, (0, 2, 1))
    print(a1)

    print('jki:')
    a2 = np.transpose(a, (1, 2, 0))
    print(a2)

    print('ikj:')
    a3 = np.transpose(a, (2, 1, 0))
    print(a3)

    print('kji:')
    a4 = np.transpose(a, (1, 0, 2))
    print(a4)

    print('kij:')
    a5 = np.transpose(a, (2, 0, 1))
    print(a5)

    print("a(ijk):")
    a_s = a + a1 + a2 + a3 + a4 + a5
    print(a_s)

    print("a[ijk]:")
    a_a = a - a3 + a2 - a1 + a5 - a4
    print(a_a)

    print("a(i|j|k):")
    a_4 = a + a4
    print(a_4)

    print("ai[jk]:")
    a_5 = a - a3
    print(a_5)

if __name__ == '__main__':
    # con()
    trt()
