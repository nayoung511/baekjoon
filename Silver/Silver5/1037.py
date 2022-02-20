def main():
    n = int(input())
    factor = list(map(int, input().split()))
    factor.sort()

    if len(factor) % 2 != 0:
        print(factor[int(len(factor)/2)] * factor[int(len(factor)/2)])

    else:
        print(factor[0] * factor[-1])

main()