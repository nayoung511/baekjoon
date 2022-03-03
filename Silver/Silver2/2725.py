import sys
input = sys.stdin.readline


def gcd(a, b):
    while (b):
        a, b = b, a % b
    return a


c = int(input())
num = [0 for _ in range (1001)]
num[1] = 3

for i in range (2, 1001):
    count = 0
    for j in range (1, i+1):
        # 약분 될 수 없으면
        if (gcd(i, j) == 1):
                count += 2
    num[i] = num[i-1] + count



for _ in range (c):
    n = int(input())

    print(num[n])
