import numpy as np


def merge(X, Y):
    merged = []
    xpointer, ypointer = 0, 0
    while xpointer < len(X) and ypointer < len(Y):
        if X[xpointer] < Y[ypointer]:
            merged.append(X[xpointer])
            xpointer += 1
        else:
            merged.append(Y[ypointer])
            ypointer += 1
    merged.extend(X[xpointer:])
    merged.extend(Y[ypointer:])
    return merged


def mergesort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
        together = merge(left, right)
        return together


if __name__ == "__main__":
    X = [1, 2, 4, 5, 7, 9]
    Y = [2, 3, 5, 6, 8, 10, 13, 17]
    print(merge(X, Y))
    print(merge(Y, X))
    Z = np.random.randint(0, 100, 100)
    print(Z)
    print(mergesort(Z))
    assert mergesort(Z) == sorted(Z)
