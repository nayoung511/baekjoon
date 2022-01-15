from collections import deque

def bfs(friends, start, visited):
    step = 0    
    queue = deque([start])
    visited[start] = True

    while queue:
        print(step, visited)
        v = queue.popleft()
        for i in friends[v]:
            print(i, friends[v])
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    
    return step

n, m = map(int, input().split())

friends = [[] for _ in range (n+1)]
visited = [False] * (n+1)

for _ in range (m):
    f1, f2 = map(int, input().split())

    #양뱡향 그래프
    friends[f1].append(f2)
    friends[f2].append(f1)

print(friends)

step = bfs(friends, 1, visited)

print(step, visited)



