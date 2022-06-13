"""
상근 승리
1, 3, 4, 5개가 남았을 때

창영 승리

"""

n = int(input())

dp = [0 for i in range (n+1)]
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1
dp[5] = 1

for i in range (6, n+1):
    dp[i] = 0
    if dp[i-1] == 0: dp[i] = 1
    if dp[i-3] == 0: dp[i] = 1
    if dp[i-4] == 0: dp[i] = 1

if dp[n] == 1:
    print("SK")
else:
    print("CY")
    
