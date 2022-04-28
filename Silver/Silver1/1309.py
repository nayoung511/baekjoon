import sys

n = int(input())

dp = [0] * (n+1)
dp[0] = 3

def cage(n):
    if n == 1:
        dp[n] = (dp[n-1] * 2) + 1
    else:
        dp[n] = ((dp[n-1] * 2) + dp[n-2]) % 9901

for i in range (1, n):
    cage(i)

print(dp[n-1])