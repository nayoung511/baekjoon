import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
soldier = [list(input().rstrip()) for i in range (m)]
visited = [[False for i in range (n)] for i in range (m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, team):
    count = 0
    q = deque([])
    q.append((x, y))

    while q:
        ex, ey = q.pop()
        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if soldier[nx][ny] == team and visited[nx][ny] == False:
                    count += 1

                    visited[nx][ny] = True
                    q.append((nx, ny))

    if count == 0:
        return 1
    return count
                
count_w = []
count_b = []
for i in range (m):
    for j in range (n):
        if visited[i][j] == False:
            if soldier[i][j] == 'W':
                count_w.append(bfs(i, j, 'W'))

            if soldier[i][j] == 'B':
                count_b.append(bfs(i, j, 'B'))

# w, b
ans = [0, 0]
for i in range (len(count_w)):
    ans[0] += count_w[i] ** 2

for i in range (len(count_b)):
    ans[1] += count_b[i] ** 2

print(*ans)