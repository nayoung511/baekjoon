from sys import stdin

n = int(input())
num = list(map(int, stdin.readline().split()))

dp = [0] * n
dp[0] = num[0]
check = dp[0]
count = 0

for i in range (1, n):
    #print(check, num[i])
    a = max(check, num[i])
    if a == num[i]:
        dp[i] = num[i]
        check = dp[i]

    #print(dp)


for i in range (n):
    if dp[i] != 0:
        count+=1

print(count)