import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph=[[] for _ in range (n+1)]
visited = [False for _ in range (n+1)]
order = [0 for _ in range (n+1)] # 방문 순서 기록


for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = [1]

#그래프를 내림차순으로
for edge in graph:
    edge.sort(reverse=True)

def dfs(r):
    # 현재 들어온 r을 방문처리 해준다 
    visited[r] = True
    order[r] = count[0]

    # 방문 순서 증가
    count[0] += 1
    for i in graph[r]: # 인접한 노드들을,
        if visited[i] == False:
            dfs(i)

dfs(r)

# 방문순서 출력
for i in range (1, len(order)):
    print(order[i])
