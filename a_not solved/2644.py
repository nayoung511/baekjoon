import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())
m = int(input())
table = [[0 for i in range (n+1)] for i in range (n+1)]
visit = [[0 for i in range (n+1)] for i in range (n+1)]

for _ in range (m):
    c, d = map(int, input().split())
    table[c][d] = 1
    table[d][c] = 1 

def printP():
    for i in range (n+1):
        for j in range (n+1):
            print(visit[i][j], end=' ')
        print()

def printJ():
    for i in range (n+1):
        for j in range (n+1):
            print(table[i][j], end=' ')
        print()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0
def bfs(x, y):
    global count
    q = deque([])
    q.append((x, y))
    count = 1

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<=n and 0<=ny<=n:
                if visit[nx][ny] == 0 and table[nx][ny]==1:
                    visit[nx][ny] = count
                    count+=1
                    print("coount", count)
                    q.append((nx, ny))

    



for i in range (n+1):
    for j in range (n+1):
        if table[i][j] == 1:
            bfs(i, j)



printP()
print("--------------")
printJ()

print(count)
