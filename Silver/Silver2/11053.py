# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열

from sys import stdin

n = int(input())
num = list(map(int, stdin.readline().split()))
# 길이를 담을 수열
dp = [0 for _ in range (n)]


for i in range (n):
    for j in range (i):
        # 다음 수가 전 수보다 증가하는가?
        if num[i] > num[j] and dp[j] > dp[i]:
                dp[i] = dp[j]


    dp[i] += 1

print(max(dp))