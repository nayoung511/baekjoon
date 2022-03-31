#### 풀기
import sys
input = sys.stdin.readline

INF = 1001
n, e = map(int, input().split())
table = [[INF for i in range (n+1)] for i in range (n+1)]
visited = [False for i in range (n+1)]
for _ in range (e):
    a, b, c = map(int, input().split())
    table[a][b] = c
    table[b][a] = c

v1, v2 = map(int, input().split())

print(table)

# 1 번 정점에서 N번으로 이동

# 거쳐가기
for k in [v1, v2]:
    # # 출발
    # for i in range (1, n+1):
    #     # 도착
    #     for j in range (1, n+1):
    print(table[1][n])
    table[1][n] = min(table[1][v1] + table[k][v2]+table[k][n], table[1][n])
    visited[k] = True

print(visited)
print(table)