from collections import deque
# col, row
n, m = map(int, input().split())
graph = []

for _ in range (n):
    graph.append(list(map(int, input())))

# 시작점부터
# E W N S
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐를 생성해서 포인트 확인 
    # 시작점 포함
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()

        # 동서남북 pt가 있는지 확인
        for k in range (4):
            # set new coordinate
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위 안인지 확인
            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] +1
                    q.append((nx, ny))

    return graph[n-1][m-1]
 
print(bfs(0,0))