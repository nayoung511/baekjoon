#
# 할 수 있음! 
# 
#

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for i in range (n)]


maxx = max(max(graph))
countMax = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def printP():
    for i in range (n):
        for j in range (n):
            print(visit[i][j], end=' ')
        print()
    print()

def calSafe():
    count = 0
    for i in range (n):
        for j in range (n):
            if visit[i][j] == False:
                count+=1
                q = deque([])
                q.append((i, j))

                while q:
                    ex, ey = q.popleft()

                    for i in range (4):
                        nx = ex + dx[i]
                        ny = ey + dy[i]

                        # 범위
                        if 0<=nx<n and 0<=ny<n:
                            if visit[nx][ny] == False:
                                visit[nx][ny] = True
                                #q.append((nx, ny))

    printP()
    print(count)
    return count


def bfs(x, y, height):
    global countMax
    q = deque([])
    q.append((x, y))

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            # 범위
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny] == False:
                    if graph[nx][ny] <= height:
                        visit[nx][ny] = True
                        q.append((nx, ny))



    val = calSafe() 
    if val > countMax:
        countMax = val


for i in range (4, 5):
    # i 이하는 잠김
    print(i)
    visit = [[False for a in range (n)] for b in range (n)]
    for j in range (n):
        for k in range (n):
            if graph[j][k] <= i:
                print(j, k, i)
                visit[j][k] = True
                bfs(j, k, i)


print(countMax)