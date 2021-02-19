def main():
    a = int(input())
    f = {}
    l = list(map(int, input().split()))

    b = int(input())
    m = list(map(int, input().split()))

    for i in range(b):
        if (m[i] in l):
            f[i] = 1
        else:
            f[i] = 0

    for i in range(b):
        print(f.get(i))

main()