import sys
sys.setrecursionlimit(10**6)

a = [0] * (10**6)

def dp(x):
    if x== 1: return 0
    if x == 2: return 0
    if x == 3: return 2
    if a[x] != 0 and x != 1 and x!= 2: return a[x]
    else:
        a[x] = dp(x-1) + dp(x-2) + dp(x-3)
    return a[x]

n = int(input())

for _ in range(n):
    x = int(input())
    if dp(x) > 100000009:
        print(dp(x) // 1000000009)
    else:
        print(dp(x))


