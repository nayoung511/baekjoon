import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
tomato = [ 0 for _ in range (m)]
#visited = [[False for _ in range (n)] for _ in range (m)]
#print(visited)
for i in range (m):
    tomato[i] = list(map(int, input().split()))

#print(tomato)
answer = 0
full_grown = [[1 * (n)]*(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    count = -1
    q = deque([])

    for i in range (m):
        for j in range (n):
            if tomato[i][j] == 1:
                q.append((i, j))
                

    while q:
        #print("length", len(q))
        for _ in range (len(q)):
            ex, ey = q.popleft()
            #print(ex, ey)

            for i in range (4):
                nx = ex + dx[i]
                ny = ey + dy[i]

                if 0<=nx<m and 0<=ny<n:
                    if tomato[nx][ny] == 0:
                        #print("true")
                        tomato[nx][ny] = 1
                        q.append((nx, ny))

        count+=1

    return count


ans = bfs()
for i in range (m):
    for j in range (n):
        if tomato[i][j] == 0:
            ans = -1

print(ans)



