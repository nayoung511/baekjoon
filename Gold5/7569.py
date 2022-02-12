import sys
from collections import deque

input = sys.stdin.readline

# m = 상자의 가로칸
# n = 상자의 세로칸
# h = 상자의 수 
m,n,h = map(int, input().split())

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

box = [[] for _ in range (h)]

# visited = [[[False]*m for _ in range (n)] for _ in range (h)]

def bfs():
    count = -1
    q = deque([])
    full_grown = True

    for i in range (h):
        for j in range (n):
            for k in range (m):
                if box[i][j][k] == 1:
                    q.append((i, j, k))
                # elif box[i][j][k] == 0:
                #     # 토마토가 다 익으면
                #     num_tomato += 1
    
    while q:
        for _ in range (len(q)):
            ez, ey, ex = q.popleft()

            for i in range (6):
                # set new coordinate
                nx = ex + dz[i]
                ny = ey + dy[i]
                nz = ez + dx[i]

                if 0<=nx<m and 0<=ny<n and 0<=nz<h:
                    if box[nz][ny][nx] == 0: # and visited[nz][ny][nx] == False:
                        box[nz][ny][nx] = 1
                        #visited[nz][ny][nx] = True
                        q.append((nz, ny, nx))

        count+=1


    #depth
    for i in range (h):
        # 세로 
        for j in range (n):
            # 가로
            for k in range (m):
                if box[i][j][k] == 0:
                    count = -1

    return count



for i in range (h):
    for j in range (n):
        box[i].append(list(map(int, input().split())))



print(bfs())




