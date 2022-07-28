import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# 0(북) 1(동) 2(남) 3(서)
r, c, d = map(int, input().split())
room = []
for i in range (n):
    room.append(list(map(int, input().split())))

visited = [[False for i in range (m)] for i in range (n)]
# 왼쪽 먼저
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    count = 1
    q = deque([(x, y)])

    while q:
        ex, ey = q.pop()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if room[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    count += 1
                    q.append((nx, ny))

    return count


bfs(r, c)

