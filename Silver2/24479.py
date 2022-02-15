import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m, r = list(map(int, input().split()))
graph=[[] for _ in range (n+1)]

for _ in range (m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for e in graph:
    e.sort()

print(graph)
idx = 1
flag = False
def dfs(idx, r):
    # 들어오는 순서
    visited[r] = True
    #idx += 1
    ans[r] = count[0]
    
    print("I visited ", r, "idx is", count[0], end = '\n')
    #ans.append(r)
    print(graph[r])
    for i in graph[r]:
        print(i, "from", graph[r])
        if visited[i] == False:
            count[0]+=1
            print("ddd", idx)
            dfs(count[0], i)
        else:
            print(i," is visited")
            

count = [1]
visited = [False for _ in range (n+1)]
ans = [0 for _ in range (n+1)]
dfs(count[0], r)
print(visited)
print("ans", ans)

for i in range(1, len(visited)):
    print(ans[i])
