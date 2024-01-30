N = 1000000


def is_prime(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


with open("primes2.txt", "w") as f:
    for i in range(2, N):
        if is_prime(i):
            f.write(str(i) + "\n")
