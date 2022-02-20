n = int(input())
dp = []
day = []
pay = []

for i in range (n):
    t, p = map(int, input().split())
    day.append(t)
    pay.append(p)
    dp.append(p)
dp.append(0)

for i in range (n-1, -1, -1):
    if day[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], pay[i] + dp[i + day[i]])

print(dp[0])


