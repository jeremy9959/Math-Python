import sys

N = 10000000
L = {1: 0}
if len(sys.argv) > 1:
    N = int(sys.argv[1])
print(f"Sieving up to {N}...")

for d in range(2, N):
    if L.get(d, 0) == 0:
        for i in range(d * d, N, d):
            L[i] = 1

if __name__ == "__main__":

    while True:
        x = int(input(f"Enter a positive number less than {N} (or 0 to quit): "))
        if x >= N or x < 0:
            print("Entry out of range")
            continue
        if x == 0:
            break
        if x == 1:
            print("Unit")
        if L.get(x, 0) == 0:
            print("Prime")
        else:
            print("Composite")
