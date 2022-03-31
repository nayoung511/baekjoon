import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num = [list(map(int, input().split())) for i in range (n)]
visited = [[False for i in range (n)] for j in range (n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, eat, count, baby):
    q = deque()
    q.append((x, y))

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            # 범위 체크
            if 0<nx<n and 0<ny<n and visited[nx][ny] == False:
                print("hello")
                if num[nx][ny] == 0:
                    count += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    

                elif 0 < num[nx][ny] < baby:
                    visited[nx][ny] = True
                    eat += 1
                    count += 1
                    if eat == baby:
                        baby += 1
                        eat = 0

                    q.append((nx, ny))

    print(count)
                    
                    


# 가장 처음 아기 상어의 크기 = 2 
count = 0
eat = 0
baby = 2
for i in range (n):
    for j in range (n):
        if num[i][j] == 9:
            visited[i][j] = True
            bfs(i, j, eat, count, baby)

print(visited)

