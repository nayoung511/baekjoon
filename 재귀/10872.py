def factorial(N):
    if N == 1:
        return N
    elif N == 0:
        return 1
    else:
        return N * factorial(N-1)


def main():
    N = int(input())
    print(factorial(N))

main()