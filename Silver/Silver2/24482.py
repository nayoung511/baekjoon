# dfs
import sys
from collections import deque
input = sys.stdin.readline
#  인접 정점은 오름차순으로 방문한다.

def dfs(start, depth):
    q = deque([(start, 0)])
    
    while q:
        current_node, depth = q.pop()

        if visited[current_node] == False:
            visited[current_node] = True
            weight[current_node] = depth

            for node in graph[current_node]:
                if not visited[node]:
                    q.append([node, depth+1])

# 정점의 수, 간선의 a수
n, m, r = map(int, input().split())
graph = [[] for i in range (n+1)]

for i in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range (n+1):
    graph[i].sort()

visited = [False for _ in range (n+1)]
weight = [0 for _ in range (n+1)]
dfs(r, 0)
for i in range (1, n+1):
    if visited[i]: print(weight[i])
    else: print(-1)