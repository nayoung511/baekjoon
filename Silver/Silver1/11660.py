import sys
input = sys.stdin.readline

# 표의 크기 n
# 합을 구해야 하는 횟수 m
n, m = map(int, input().split());

num = [list(map(int, input().split())) for i in range (n)]
netSum = [[0 for i in range(n + 1)] for i in range(n + 1)]

for i in range (n):
    for j in range (n):
        netSum[i + 1][j + 1] = netSum[i][j + 1] + netSum[i + 1][j] - netSum[i][j] + num[i][j];

print(netSum)

for i in range (m):
    x1, y1, x2, y2 = map(int, input().split())
    print(netSum[x2][y2] - (netSum[x1 - 1][y2] + netSum[x2][y1 - 1] - netSum[x1 - 1][y1 - 1]))