from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = 1
    
    # 큐가 빌 때까지 반복
    while queue:
        #print(queue, visited)
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        #print(v, end=' ')

        #아직 방문하지 않은 인접한 원소들을 큐에 삽입

        #print("graph[v]", graph[v])
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

def main():
    n = int(input())
    m = int(input())

    graph=[[] for _ in range(n+1)]
    #print(graph)

    for i in range (m):
        source, destination = map(int, input().split())

        # 양뱡향 그래프
        graph[source].append(destination)
        graph[destination].append(source)

    #print(graph)

    visited = [0] * (n+1)

    bfs(graph, 1, visited)

    count = 0

    for i in range (len(visited)):
        if visited[i] == 1:
            count+=1

    print(count-1)


main()