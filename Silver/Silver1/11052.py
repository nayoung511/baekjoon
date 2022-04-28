import sys
input = sys.stdin.readline

n = int(input()) # 구매하려고 하는 카드 개수
card = list(map(int, input().split()))
card.insert(0, 0)
dp = [0 for i in range (n+1)]

for i in range (1, n+1):
    for j in range (1, i+1):
        dp[i] = max(dp[i-j]+card[j], dp[i])

print(dp[-1])