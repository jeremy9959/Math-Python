from functools import lru_cache


# @lru_cache(maxsize=100)


def fib(n):
    assert n >= 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    assert n >= 0
    f1, f0 = 1, 0
    for i in range(2, n + 1):
        f1, f0 = f1 + f0, f1
    return f1


if __name__ == "__main__":
    n = input("Enter n: ")
    n = int(n)
    print(f"F{n} = {fib(n)}")
