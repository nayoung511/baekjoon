import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range (n):
    graph.append(list(map(str, input())))

check = deque([])
visit = [[0 for i in range (n)] for _ in range (m)]
maxx = 0

def dfs(x, y):
    global maxx
    # 범위 체크
    if x < 0 or x > n or y < 0 or y > m:
        return False

    if len(check) > maxx:
        maxx = len(check)
        print(check)

    # 방문하지 않은 노드라면
    if visit[x][y] == 0:
        # 방문하지 않은 알파벳이라면
        if graph[x][y] not in check:
            print(x, y, graph[x][y])
            check.append(graph[x][y])
            # 방문처리
            visit[x][y] = 1
            # 이웃 노드 방문
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x, y+1)

        else:
            if len(check) > 0:
                check.pop()

dfs(0, 0)

print(visit)
print(check)
print(maxx)