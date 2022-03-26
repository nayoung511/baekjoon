import sys
from collections import deque
input = sys.stdin.readline
max_b=100001

def bfs(n):
    q = deque([n])
    visited[n][0] = 1   # 방문처리
    visited[n][1] = 0   # 시간 = 0으로 설정

    while q:
        x = q.popleft()

        # 1초 후에 X-1, X+1, 2*X
        # 2*X = 0초, +-1 = 1초
        if x * 2 <= max_b and visited[x*2][0] == 0:
            q.appendleft(x*2)
            visited[x*2][0] = 1 # 방문처리
            visited[x*2][1] = visited[x][1]
        # x+1
        if x + 1 <= max_b and visited[x+1][0] == 0:
            q.append(x+1)
            visited[x+1][0] = 1 # 방문처리
            visited[x+1][1] = visited[x][1] + 1

        # x-1
        if x - 1 >= 0 and visited[x-1][0] == 0:
            q.append(x-1)
            visited[x-1][0] = 1 # 방문처리
            visited[x-1][1] = visited[x][1] + 1

# n = 수빈이 있는 위치
# k = 동생이 있는 위치
n, k = map(int, input().split())
# [방문, 시간]
# 방문 = 0 (false), 1 (true)
visited= [[0, -1] for _ in range (max_b+1)]

bfs(n)
print(visited[k][1])
