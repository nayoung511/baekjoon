def main():
    a, b = input().split()

    a = int(a)
    b = int(b)

    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    final = list()

    final = first + second
    final.sort()

    result = ' '.join([str(e) for e in final])

    print(result)
    


main()