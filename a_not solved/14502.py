import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

num=[i for i in range (n)]
for i in range (n):
    num[i] = list(map(int, input().split()))



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    wall = 3
    q = deque()
    for i in range (n):
        for j in range (m):
            if num[i][j] == 0:
                q.append((i, j))

    while q:
        ex, ey = q.popleft()
        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            # 범위
            if 0<=nx<n and 0<=ny<m:
                # 아직 세울 수 있는 벽이 남아 있을 때
                if wall > 0 and num[nx][ny] == 0:
                    num[nx][ny] = 1
                    wall -= 1

bfs()
print(num)
# 벽 갯수 3개
count = 0
for i in range (n):
    for j in range (m):
        if num[i][j] == 0:
            count+=1

print(count)                    


            

