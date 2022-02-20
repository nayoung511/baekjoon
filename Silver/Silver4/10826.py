import sys
sys.setrecursionlimit(10**6)

n = int(input())
x = [0] * 10001

def dp(n):
    if n == 0: return 0
    if n == 1: return 1
    if x[n] != 0: return x[n]
    else:
        x[n] = dp(n-1) + dp(n-2)
    return x[n]

print(dp(n))