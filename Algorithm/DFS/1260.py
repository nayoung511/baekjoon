import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    
    for i in range (1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)


def dfs_recursive(graph, start_node, visited = []):
    visited.append(start_node)

    for node in graph[start_node]:
        if node not in visited:
            dfs_recursive(graph, node, visited)

    return visited

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range (n+1)]
for i in range (m):
    a, b, = map(int, input().split())
    # 간선간의 관계 - edge가 있으면 서로 1
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False for i in range (n+1)]
dfs(graph, v, visited)
