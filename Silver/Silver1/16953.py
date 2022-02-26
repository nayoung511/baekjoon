import sys
input = sys.stdin.readline

a, b = (map(int, input().split()))
count = 0

while b > a:
    if b % 2 == 0:
        b = b // 2
        count += 1

    elif b % 10 == 1:
        b = b // 10
        count += 1
    else:
        break


if b == a:
    count += 1
    print(count)
else:
    print(-1)
