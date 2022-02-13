import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
# 가장 긴 감소하는 수열 == 가장 긴 증가하는 수열 in reverse
num.reverse()
dp = [0 for _ in range (n+1)]
dp[0] = 1
print(num)

for i in range (1, n): # next
    for j in range (i): # current
        print(i, j, num[i], num[j], dp[i-1])
        if num[i] > num[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1
    print(dp)
print(max(dp))