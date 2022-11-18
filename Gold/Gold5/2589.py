import sys
from collections import deque
input = sys.stdin.readline

treasure = []
l, w = map(int, input().split())
for i in range (l):
    treasure.append(list(map(str, input().rstrip())))

visited = [[False for i in range (w)] for j in range (l)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

#find out where the furthest treasures are located
def bfs_furthest_treasure(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    count = 0

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<l and 0<=ny<w:
                if treasure[nx][ny] == 'L' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    count += 1
                    q.append((nx, ny))
                    px = nx
                    py = ny

    return count, px, py

maxx_count = 0
end_treasure_x = 0
end_treasure_y = 0
for i in range (l):
    for j in range (w):
        if treasure[i][j] == 'L' and visited[i][j] == False:
            ans = bfs_furthest_treasure(i, j)
            if ans[0] > maxx_count:
                maxx_count = ans[0]
                end_treasure_x = ans[1]
                end_treasure_y = ans[2]

print(end_treasure_x, end_treasure_y)

visited_from_end = [[False for i in range (w)] for j in range (l)]
step = [[0 for i in range(w)] for j in range (l)]
def bfs(x, y):
    count = 0
    q = deque([(x, y)])
    visited_from_end[x][y] = True

    while q:
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0<=nx<l and 0<=ny<w:
                if treasure[nx][ny] == 'L' and visited_from_end[nx][ny] == False:
                    if step[nx][ny] < 
                    visited_from_end[nx][ny] = True
                    count += 1
                    q.append((nx, ny))


    return count


minn_count = maxx_count
minn_count = min(bfs(end_treasure_x, end_treasure_y), minn_count)
print(minn_count)

