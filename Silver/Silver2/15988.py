import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range (1000001)]
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range (3, 1000001):
    dp[i] = (dp[i-1] % 1000000009 + dp[i-2] % 1000000009 + dp[i-3] % 1000000009)


for _ in range (n):
    a = int(input())
    print(dp[a-1] % 1000000009)