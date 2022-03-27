import sys
from collections import deque
input = sys.stdin.readline
max_b=100000

def route(n):
    arr = []
    temp = n
    for _ in range (visited[n][0] + 1):
        arr.append(temp)
        temp = visited[temp][1]
    print(' '.join(map(str, arr[::-1])))

def bfs(n):
    q = deque([n])

    while q:
        x = q.popleft()
        if x == k:
            print(visited[k][0])
            # 경로 계산
            route(x)
            break

        for i in (x+1, x-1, x*2):
            if 0<= i < max_b and visited[i][0] == 0:
                q.append(i)
                visited[i][0] = visited[x][0] + 1
                visited[i][1] = x


# n = 수빈이 있는 위치
# k = 동생이 있는 위치
n, k = map(int, input().split())
visited= [[0, 0] for _ in range (max_b)]

bfs(n)