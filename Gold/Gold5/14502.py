import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range (n)]

maxx = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
virus_list = []
for i in range (n):
    for j in range (m):
        if graph[i][j] == 2:
            virus_list.append([i, j])

def wall(start, count):
    global maxx
    if count == 3:
        selNM = copy.deepcopy(graph)
        for i in range (len(virus_list)):
            x, y = virus_list[i]
            spread_virus(x, y, selNM)
        c = sum(j.count(0) for j in selNM)
        maxx= max(maxx, c)
    else:
        for i in range (start, n*m):
            x = i // m
            y = i % m
            if graph[x][y] == 0:
                graph[x][y] = 1
                wall(i, count+1)
                graph[x][y] = 0

def spread_virus(x, y, selNM):
    if selNM[x][y] == 2:
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if selNM[nx][ny] == 0:
                    selNM[nx][ny] = 2
                    spread_virus(nx, ny, selNM)


wall(0,0)
print(maxx)