import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
letter = []
for i in range (m):
    letter.append(list(map(int, input().split())))

visited = [[False for i in range (n)] for i in range (m)]

# 상하좌우, 대각선
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

count = 0
def bfs(i, j):
    global count
    count += 1
    q = deque([])
    q.append((i, j))

    while q:
        ex, ey = q.pop()

        for i in range (8):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if letter[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return count


for i in range (m):
    for j in range (n):
        if visited[i][j] == False:
            if letter[i][j] == 1:
                bfs(i, j)

print(count)
