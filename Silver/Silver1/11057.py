n = int(input())

dp = [[1 for i in range (10)] for j in range (n)]
for i in range (1, n):
    for j in range (1, 10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[n-1]) % 10007)