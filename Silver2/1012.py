from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, -0, 0]

def bfs(graph, i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0

    while q:
        ex, ey = q.popleft()
        #동서남북
        for k in range (4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

    return

for _ in range (t):
    cnt = 0
    n, m, k = map(int, input().split())
    chk = [[0] * (m) for _ in range (n)]

    for _ in range (k):
        x, y = map(int, input().split())
        chk[x][y] = 1

    for i in range (n):
        for j in range (m):
            if chk[i][j] == 1:
                bfs(chk, i, j)
                cnt+= 1

    print(cnt)
