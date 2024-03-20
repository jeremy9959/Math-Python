import inspect


def pow(x, k, N):
    # F = inspect.currentframe()

    # print(f"Entering with x={x}, k={k}, N={N} from line {F.f_back.f_lineno}")
    if k == 0:
        result = 1
    elif k % 2 == 0:
        result = pow(x * x % N, k // 2, N)
    else:
        result = x * pow(x, k - 1, N) % N

    # print(
    #     f"Returning with x ={x}, k ={k}, N ={N}, returning {result} to line {F.f_back.f_lineno}"
    # )
    return result


def mypow(x, k, N):
    stack = []
    while True:
        if k == 0:
            stack.append((1, x, 0, N))
            break
        elif k % 2 == 0:
            stack.append((1, x * x % N, k // 2, N))
            k = k // 2
            x = x * x % N
            continue
        else:
            stack.append((x, x, k - 1, N))
            k = k - 1
            continue
    answer = 1
    print(f"Stack has length {len(stack)}")
    while stack:
        result, x, k, N = stack.pop()
        answer = answer * result % N
    return answer


def fermat(x, N):
    return pow(x, N - 1, N) == 1


if __name__ == "__main__":
    base = input("Enter the base for the Fermat test: ")
    base = int(base)
    modulus = input("Enter the modulus for the Fermat test: ")
    modulus = int(modulus)
    # if fermat(base, modulus):
    #     print(base, "is a Fermat witness for", modulus)
    # else:
    #     print(base, "is not a Fermat witness for", modulus)
    print(mypow(base, modulus - 1, modulus))
    print(pow(base, modulus - 1, modulus))
