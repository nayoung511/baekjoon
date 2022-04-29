import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range (10001)]
dp[0] = 1
dp[1] = 2
dp[2] = 3


for i in range (3, 10001):
    dp[i] = dp[i-3] + ((i+1)//2) + 1

for _ in range (n):
    print(dp[int(input())-1])


"""
n = 4 --> 4
1+1+1+1
2+1+1
2+2
3+1

n = 5 --> 6
1+1+1+1+1
1+1+1+2
1+2+2
3+2
3+1+1

n = 6 --> 7
1+1+1+1+1+1
1+1+1+1+2
1+1+2+2
2+2+2
1+1+1+3
1+2+3
3+3


n = 7 --> 8

"""