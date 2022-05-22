import sys
from collections import deque
input = sys.stdin.readline

dp = []

n, m = map(int, input().split())
for _ in range (n):
    dp.append(list(map(int, input().split())))

dx = [1, 0, 1]
dy = [0, 1, 1]
summ = dp[0][0]

# dp = [[0 for _ in range (m)] for _ in range (n)]
# dp[0][0] = graph[0][0]

visited = []
def dpCal(x, y):
    for i in range (3):
        nx = dx[i] + x
        ny = dy[i] + y

        if [nx, ny] not in visited:
            if 0<=nx<n and 0<=ny<m:
                dp[nx][ny] += max(dp[nx-1][ny], dp[nx][ny-1], dp[nx-1][ny-1])
                visited.append([nx, ny])

dpCal(0, 0)
print(dp)

# def bfs(x, y):
#     global summ
#     visited=[]
#     q = deque()
#     q.append((x, y))
    
#     while q:
#         print(summ)
#         ex, ey = q.pop()

#         for i in range (3):
#             nx = dx[i] + ex
#             ny = dy[i] + ey

#             if [nx, ny] not in visited:
#                 if 0<=nx<n and 0<=ny<m:
#                     print("im", nx, ny, "value", graph[nx][ny])
#                     if nx == n and ny == m:
#                         return
#                     summ += graph[nx][ny]
#                     q.append((nx, ny))
#                     visited.append([nx, ny])

# bfs(0,0)
# print(summ)

