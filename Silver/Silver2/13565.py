import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True

    for i in range (4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 체크
        if 0<=nx<n and 0<=ny<m:
            # 전류가 흐르는 곳이라면
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                # 방문처리
                visited[nx][ny] = True
                dfs(nx, ny)
        

n, m = map(int, input().split())
visited = [[False for i in range (m)] for _ in range (n)]
graph = []

for _ in range (n):
    graph.append(list(map(int, input().rstrip())))

# 격자의 위쪽 아무 index에서 출발
# 0 = 전류가 통함
# 1 = 전류가 통하지 않음
flag = False
for i in range (m):
    if graph[0][i] == 0:
        dfs(0, i)
        
for i in range (m):
    # 맨 끝까지 전류가 닫는 곳이 있다면
    if visited[-1][i] == True:
        flag = True

if flag == False:
    print("NO")
else:
    print("YES")
