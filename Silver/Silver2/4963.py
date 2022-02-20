import sys
from collections import deque
input = sys.stdin.readline


# 가로, 세로, 대각선
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True
    #land = 0

    while q:
        # 큐에 있는 원소를 하나씩 pop해서 확인
        ex, ey = q.popleft()

        # 8개의 direction 확인
        for i in range (8):
            # new coordinate
            nx = ex + dx[i]
            ny = ey + dy[i]

            #print("nx", nx, "ny", ny)

            # check boundary
            if 0 <= nx < h and 0<= ny < w:
                # 방문하지 않았다면 
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    #land += 1
                    q.append((nx, ny))

    #return land

while True:
    num = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    # create map
    graph = []
    visited = [[False for i in range (w)] for j in range (h)]
    #print(graph)

    # 1일 경우
    if h == 1:
        a = int(input())
        if a == 0:
            print(0)
        else:
            print(1)

    else:
        for i in range (h):
            graph.append(list(map(int, input().split())))

        #print(graph)

        for i in range (h):
            for j in range (w):
                if visited[i][j] == False and graph[i][j] == 1:
                    bfs(i, j)
                    num += 1

        print(num)



    
