import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
# 가장 긴 감소하는 수열 == 가장 긴 증가하는 수열 in reverse
num.reverse()
dp = [0 for _ in range (n)]
dp[0] = 1
print(num)

for i in range (1, n): # next
    for j in range (i): # current
        print(j, i, num[j], num[i])
        if num[i] > num[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

            print("before", dp)

    

    dp[i] += 1
    print(dp, "\n")
print(max(dp))