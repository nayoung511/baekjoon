# bfs
import sys
from collections import deque
input = sys.stdin.readline

# 양 #
# 풀 .

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, h, w, visited):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        ex, ey = q.pop()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<h and 0<=ny<w:
                if visited[nx][ny] == False and grid[nx][ny] == '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))


t = int(input())
for _ in range (t):
    h, w = map(int, input().split())

    grid = []
    
    for _ in range (h):
        grid.append(list(map(str, input().rstrip())))
    
    visited = [[False for _ in range (w)] for _ in range (h)]
    count = 0

    for i in range (h):
        for j in range (w):
            if visited[i][j] == False:
                if grid[i][j] == '#':
                    bfs(i, j, h, w, visited)
                    count += 1

    print(count)


