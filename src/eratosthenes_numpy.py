import numpy as np

N = 1000000
L = np.zeros(N)

with open("primes.txt", "w") as f:
    for d in np.arange(2, N):
        if L[d] == 0:
            f.write(str(d) + "\n")
            for i in np.arange(d * d, N, d):
                L[i] = 1
