from collections import deque
import sys
input = sys.stdin.readline

q = deque([])

# vertex, edge
n, m = map(int, input().split())
graph=[[] for _ in range (n+1)]
connected = [False] * (n+1)

def bfs(i):
    # 큐에 원소를 집어 넣어주고
    q = deque([i])
    connected[i] = True

    while q:
        fr = q.popleft()

        for i in graph[fr]:
            # from -> to로 가는 edge가 있는지 확인 
            if not connected[i]:
                q.append(i)
                connected[i] = True
               

for i in range (m):
    fr, to = map(int, input().split())
    graph[fr].append(to)
    graph[to].append(fr)

num = 0
for i in range (1, n+1):
        if not connected[i]:
            bfs(i)
            num += 1

print(num)

