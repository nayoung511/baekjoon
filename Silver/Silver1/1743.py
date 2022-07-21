import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
garbage = [[0 for i in range (m)] for i in range (n)]
visited = [[False for i in range (m)] for i in range (n)]

# 음식물이 떨어진 좌표
for i in range (k):
    r, c = map(int, input().split())
    garbage[r-1][c-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    garbage_size = 0
    q = deque([])
    q.append((x, y))

    while q:
        ex, ey = q.pop()
        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if garbage[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    garbage_size += 1
                    q.append((nx, ny))

    return garbage_size

max_garbage_size = 0
for i in range (n):
    for j in range (m):
        if garbage[i][j] == 1 and visited[i][j] == False:
            max_garbage_size = max(max_garbage_size, bfs(i, j))

print(max_garbage_size)