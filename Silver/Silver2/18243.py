import sys
input = sys.stdin.readline
INF = 1000000

n, k = map(int, input().split())
network = [[0 for _ in range(n)] for _ in range (n)]

for i in range (k):
    a, b = map(int, input().split())
    network[a-1][b-1] = 1
    network[b-1][a-1] = 1

for i in range (n):
    for j in range (n):
        if i != j:
            if network[i][j] == 0:
                network[i][j] = INF


# 거쳐가는 노드 
for i in range (n):
    # 출발 노드
    for j in range (n):
        # 도착 노드
        for k in range (n):
            if j == k:
                continue
            if (network[j][i] + network[i][k] < network[j][k]):
                network[j][k] = network[j][i] + network[i][k]

big = False
for i in range (n):
    for j in range (n):
        # 연결 안 되어 있는 경우
        # 6 연결을 넘은 경우
        if ((network[i][j] == 0 and i !=j) or (network[i][j]) > 6):
            big = True

if big == False:
    print("Small World!")
else:
    print("Big World!")
