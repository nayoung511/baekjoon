import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range (n)]
minn = 0

def count():
    count = 0
    for i in range (n):
        for j in range (m):
            if graph[i][j] == 0:
                count += 1

    return count

# calculate first count
maxx = count()
print(maxx)
q = deque([])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def wall(x, y):
    global minn
    wall = 3
    q.append([x, y])

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<nx<n and 0<ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    wall -= 1
                    q.append([nx, ny])

        
                if wall == 0:
                    minn = count()

                    print(minn)
                    if maxx > minn:
                        return minn


for i in range (n):
    for j in range (m):
        if graph[i][j] == 2:
            wall(i, j)


print(graph)

def virus(x, y):
    q.append([x, y])

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<nx<n and 0<ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append([nx, ny])



for i in range (n):
    for j in range (m):
        if graph[i][j] == 2:
            virus(i, j)

print(count())
print(minn)