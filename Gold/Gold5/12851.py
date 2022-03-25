import sys
from collections import deque
input = sys.stdin.readline
max_b=100000

def bfs(n):
    q = deque([n])
    visited[n][0] = 0
    visited[n][1] = 1

    while q:
        x = q.popleft()

        # 1초 후에 X-1, X+1, 2*X
        for i in [x-1, x+1, x*2]:
            if 0 <= i <= max_b:
                if visited[i][0] == -1:
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] = visited[x][1]
                    q.append(i)

                elif visited[i][0] == visited[x][0] + 1:
                    visited[i][1] += visited[x][1]


# n = 수빈이 있는 위치
# k = 동생이 있는 위치
n, k = map(int, input().split())
# [k에 도달하는데 걸린 시간, 경우의 수]
visited= [[-1, 0] for _ in range (max_b+1)]

bfs(n)
print(visited[k][0])
print(visited[k][1])
