import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
tomato = [ 0 for _ in range (m)]
for i in range (m):
    tomato[i] = list(map(int, input().split()))

# BFS를 위한 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    # 날짜 세기
    count = -1
    q = deque([])

    for i in range (m):
        for j in range (n):
            # 익은 토마토라면
            if tomato[i][j] == 1:
                # 현재 좌표를 큐에 삽입
                q.append((i, j))
                

    while q:
        for _ in range (len(q)):
            ex, ey = q.popleft()

            # 현재 좌표에서 갈 수 있는 새로운 좌표를 for loop으로 구함
            for i in range (4):
                nx = ex + dx[i]
                ny = ey + dy[i]

                if 0<=nx<m and 0<=ny<n:
                    # 새로운 좌표 이웃이 안 익은 토마토라면
                    if tomato[nx][ny] == 0:
                        # 익어라
                        tomato[nx][ny] = 1
                        q.append((nx, ny))
        # 날을 추가해준다
        count+=1

    return count


ans = bfs()
for i in range (m):
    for j in range (n):
        # 안익은 토마토가 하나라도 있다면,
        if tomato[i][j] == 0:
            ans = -1

print(ans)



