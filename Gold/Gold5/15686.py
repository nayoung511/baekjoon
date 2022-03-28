import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range (n)]

print(graph)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    q = deque([x, y])

    while q:
        ex, ey = q.popleft()

        

