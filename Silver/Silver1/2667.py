import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
danji = []
apart = [list(map(int, input().rstrip())) for _ in range (n)]
visited = [[False for _ in range (n)] for _ in range (n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    count = 1
    q = deque([[x, y]])
    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            # check the range
            if 0 <= nx < n and 0 <=ny < n:
                if visited[nx][ny] == False and apart[nx][ny] == 1:
                    count+=1
                    visited[nx][ny] = True
                    q.append([nx, ny])

    #print(count)

    return count



for i in range (n):
    for j in range (n):
        cnt_danji = 0 
        if apart[i][j] == 1 and visited[i][j] ==False:
            visited[i][j] = True
            cnt_danji = 1
            ans = bfs(i, j)
            if ans != 1:
                danji.append(ans+cnt_danji-1)
            else:
                danji.append(cnt_danji)
            #print(visited)

#print(danji)
print(len(danji))
danji.sort()
for i in danji:
    print(i)