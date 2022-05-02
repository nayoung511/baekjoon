import sys
n, k = map(int, input().split())

def equa(n, a, k):
    equation = [['' for i in range(n)] for i in range (a)]

    for i in range (1, n+1):
        for j in range (i):
                equation[i][j] = j+

    print(equation)

dp = [0 for i in range (11)]
dp[0] = 1
dp[1] = 2
dp[2] = 4

# 몇 개 있는지
for i in range (3, n):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

if k > dp[n-1]:
    print(-1)
else:
    equa(n, dp[n-1], k)


