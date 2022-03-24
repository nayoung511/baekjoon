import sys
input = sys.stdin.readline

INF = 1000000000

# v = 정점, e = 간선 
v, e = map(int, input().split())
graph = [[INF for i in range (v)] for i in range (v)]
# 방문한 노드
visited = [False for i in range (v)]
# 최단 거리
dist = [0 for i in range (v)]

# 시작 정점의 번호
start = int(input())

# 간선, u -> v (w)
for i in range (e):
    u, vu, w = map(int, input().split())
    graph[u-1][vu-1] = w
    graph[i-1][i-1] = 0


def getSmallerIndex():
    minn = INF
    index = 0

    # 방문하지 않은 노드 중에서 현재 최솟값보다 작은 것이 있다면
    for i in range (v):
        if (dist[i] < minn and not visited[i]):
            minn = dist[i]
            index = i

    return index

def dijkstra(start):
    for i in range (v):
        dist[i] = graph[start-1][i]

    visited[start-1] = True
    for i in range (v-2):
        current = getSmallerIndex()
        visited[current] = True

        for j in range (v):
            if not visited[j]:
                if dist[current] + graph[current][j] < dist[j]:
                    dist[j] = dist[current] + graph[current][j] 


dijkstra(start)
for i in range (v):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])