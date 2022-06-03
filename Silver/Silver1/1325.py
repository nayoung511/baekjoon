from collections import deque

n, m = map(int, input().split())

graph = [[-1 for i in range (n)] for j in range (n)]

def printP(n, graph):
    for i in range (n):
        print(graph[i])

for _ in range (m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = b-1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != -1:
                    graph[nx][ny] = x
                    q.append((nx, ny))

printP(n, graph)
print("------------")

for i in range (n):
    for j in range (n):
        if graph[i][j] != -1:
            graph[j][i] = graph[i][j]
            printP(n, graph)
            print("-------=------")
            #print(i, j)
            #bfs(i, j)

print(graph)