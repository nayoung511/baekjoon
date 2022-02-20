import sys
sys.setrecursionlimit(10**6)

a = [0] * 11

def dp(x):
    if x== 1: return 1
    if x == 2: return 2
    if x == 3: return 4
    if a[x] != 0: return a[x]
    else:
        a[x] = dp(x-1) + dp(x-2) + dp(x-3)
    return a[x]

n = int(input())

for _ in range(n):
    x = int(input())
    print(dp(x))


