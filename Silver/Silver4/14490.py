import sys
input = sys.stdin.readline

n = list(map(int, input().split(':')))

def gcd(x, y):
    while (y):
        x, y = y, x % y

    return x

val = gcd(n[0], n[1])

print(str(n[0] // val) + ":" + str(n[1]//val))