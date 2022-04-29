import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range (10001)]
dp[0] = 1
dp[1] = 2
dp[2] = 3

def dpcal(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 3

    else:


for _ in range (n):
    dpcal(int(input()))
    print(dp[n-1])


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

n = 6 -->
1+1+1+1+1+1
1+1+1+1+2
1+1+2+2

n = 7 --> 8

"""