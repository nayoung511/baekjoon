import sys
input = sys.stdin.readline
INF = 1000000001

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

bus = [[INF for i in range (n)] for j in range (n)]
for _ in range (m):
    a, b, c = map(int, input().split())
    if (bus[a-1][b-1] != INF):
        bus[a-1][b-1] = min(bus[a-1][b-1], c)
    else: bus[a-1][b-1] = c

for k in range (n):
    for i in range (n):
        for j in range (n):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for i in range (n):
    bus[i][i] = 0
    for j in range (n):
        if (bus[i][j] == INF):
            print("0", end=' ')
        else:
            print(bus[i][j], end=' ')
    print()