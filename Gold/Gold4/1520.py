import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range (n)]
visited = [[False for i in range (m)] for i in range (n)]

def dfs(graph, i, j, visited, current):
    visited[i][j] = True
    for k in graph[i]:
        # 현재의 나보다 값이 작을 때
        if k < current:
            if not visited[i][k]:
                dfs(graph, i, k, visited)


dfs(graph, 0, 0, visited, graph[0][0])
print(visited)


