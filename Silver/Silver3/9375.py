import sys
input = sys.stdin.readline


t = int(input())
for _ in range (t):
    num = []
    d = dict()
    summ = 1

    n = int(input())

    for i in range (n):
        num.append(list(map(str, input().split())))
        if num[i][1] in d:
            d[num[i][1]] += 1
        else:
            d[num[i][1]] = 1

    for x in d:
        a = (d[x] + 1)
        summ *= a

    print(summ-1)
