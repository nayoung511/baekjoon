import sys
sys.setrecursionlimit(10**6)

a = [0] * 1001

def dp(n):
    if n == 1: return 1
    if n == 2: return 2
    if a[n] != 0: return a[n]
    else:a[n] = dp(n-1) + dp(n-2)
    return a[n]

n = int(input())


print(dp(n)%10007)