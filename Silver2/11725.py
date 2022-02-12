import sys
sys.setrecursionlimit(10 ** 9)


input = sys.stdin.readline

# 노드의 개수
n = int(input())
tree = [[] for _ in range (n+1)]
parents = [0 for _ in range (n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            #print(parents)
            DFS(i, tree, parents)

    
DFS(1, tree, parents)

for i in range (2, n+1):
    print(parents[i])