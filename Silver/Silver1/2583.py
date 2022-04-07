import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    global count
    q = [[i, j]]
    
    while q:
        x, y = q[0][0], q[0][1]
        # pop
        q.remove(q[0])
        for k in range (4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                count += 1
                q.append([nx, ny])
    cnt.append(count)

        

graph = [[0 for i in range (n)] for i in range (m)]
cnt = []

for _ in range (k):
    # 왼쪽 아래 x, y / 오른쪽 위 x, y
    x1, y1, x2, y2 = map(int, input().split())
    # 그래프 1초 바꿈
    for i in range (y1, y2):
        for j in range (x1, x2):
            graph[i][j]=1

for i in range (m):
    for j in range (n):
        # 흰 부분 발견
        if (graph[i][j] == 0):
            count = 1
            graph[i][j] = 1

            bfs(i, j)


print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end=' ')

