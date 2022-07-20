import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

color = [list(map(str, input().rstrip())) for _ in range (n)]
visited = [[0 for i in range (n)]for j in range (n)]
visitedColorblind = [[0 for i in range (n)]for j in range (n)]

countAreaNonColorblind = 0
countAreaColorblind = 0

# 색맹이 아닌 사람
def nonColorBlind(x, y, v):
    global countAreaNonColorblind
    q = deque([])
    q.append((x, y)) 

    countAreaNonColorblind += 1

    while q:
        # print(q)
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if (0<= nx < n and 0<= ny < n):
                if (visited[nx][ny] == 0):
                    if (color[nx][ny] == v):
                        visited[nx][ny] = 1
                        q.append((nx, ny))

# 색맹인 사람
# 빨강 초록을 하나로 묶어야 함
def colorBlind(x, y, v):
    global countAreaColorblind
    q = deque([])
    q.append((x, y)) 

    countAreaColorblind += 1

    while q:
        # print(q)
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if (0<= nx < n and 0<= ny < n):
                if (visitedColorblind[nx][ny] == 0):
                    if v == 'R':
                        # 빨간색이면 초록색까지 같이 체크
                        if (color[nx][ny] == v) or (color[nx][ny] == 'G'):
                            visitedColorblind[nx][ny] = 1
                            q.append((nx, ny))

                    elif v == 'G':
                        if (color[nx][ny] == v) or (color[nx][ny] == 'R'):
                            visitedColorblind[nx][ny] = 1
                            q.append((nx, ny))

                    else:
                        if (color[nx][ny] == v):
                            visitedColorblind[nx][ny] = 1
                            q.append((nx, ny))

# 색맹이 아닌 사람
for i in range (n):
    for j in range (n):
        if color[i][j] == 'R' and visited[i][j] == 0:   
            # 방문 처리
            nonColorBlind(i, j, 'R')

        if color[i][j] == 'B' and visited[i][j] == 0:   
            # 방문 처리
            nonColorBlind(i, j, 'B')

        if color[i][j] == 'G' and visited[i][j] == 0:   
            # 방문 처리
            nonColorBlind(i, j, 'G')

# 색맹인 사람
for i in range (n):
    for j in range (n):
        if color[i][j] == 'R' and visitedColorblind[i][j] == 0:   
            # 방문 처리
            colorBlind(i, j, 'R')

        if color[i][j] == 'B' and visitedColorblind[i][j] == 0:   
            # 방문 처리
            colorBlind(i, j, 'B')

        if color[i][j] == 'G' and visitedColorblind[i][j] == 0:   
            # 방문 처리
            colorBlind(i, j, 'G')


print(countAreaNonColorblind, countAreaColorblind)
