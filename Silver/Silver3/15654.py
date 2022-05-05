n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
arr = [0 for i in range (n+1)]
visited = [0 for i in range (n+1)]

def visit(k):
    if k == m:
        for i in range (m):
            print(arr[i], end=' ')
        print()


    for i in range (1, n+1):
        if (visited[i] == 0):
            arr[k] = a[i-1]
            visited[i] = 1
            visit(k+1)
            visited[i] = 0


visit(0)