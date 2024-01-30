N = 100000
L = {}

with open("primes.txt", "w") as f:
    for d in range(2, N):
        if L.get(d, 0) == 0:
            f.write(str(d) + "\n")
            for i in range(d * d, N, d):
                L[i] = 1

print(N - 2 - len(list(L.keys())))
