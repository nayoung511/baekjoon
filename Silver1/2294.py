def exchange(coin, k):
    ans = 0
    dp=[10001 for i in range (k+1)]
    dp[0] = 0

    for i in range (n):
        for j in range (coin[i], k+1):
            dp[j] = min(dp[j], dp[j-coin[i]]+1)

    if dp[k] != 10001:
        ans = dp[k]
    else:
        ans = -1
    return ans

n, k = map(int, input().split())
coin = [0] * (n)

for i in range (n):
    coin[i] = int(input())

print(exchange(coin, k))
