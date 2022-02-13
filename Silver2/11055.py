# 가장 큰 증가 부분 수열 
import sys
input = sys.stdin.readline


n = int(input())
num = list(map(int, input().split()))
dp = [0 for i in range (n+1)]
dp[0] = num[0]

maxx = dp[0]

for i in range (1, n):
    for j in range (i):
        # 다음의 수가 나보다 작을 때 
        if num[j] < num[i]:
            #print(dp[i], dp[j])
            dp[i] = max(dp[i], dp[j])

    
    #print(num[i])
    dp[i] += num[i]
    #print(dp)
    maxx = max(maxx, dp[i])

print(maxx)
