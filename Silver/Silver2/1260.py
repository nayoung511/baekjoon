def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')
    for i in range (1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = [v]
    visited[v] = False
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1, n+1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False

n, m, v = input().split()
n = int(n)
m = int(m)
v = int(v)

graph =[[0]*(n+1) for _ in range (n+1)]
for i in range (m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * len(graph)
#dfs, bfs
dfs(graph, v, visited)
print()
bfs(graph, v, visited)
