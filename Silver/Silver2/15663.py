import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
arr = [0 for i in range (n+1)]
visited = [0 for i in range (n+1)]

def visit(k):
    if k == m:
        for i in range (m):
            print(arr[i], end=' ')
        print()

    used = 0
    for i in range (1, n+1):
        if (visited[i] == 0):
            if used != a[i-1]:
                arr[k] = a[i-1]
                used = a[i-1]
                visited[i] = 1
                visit(k+1)
                visited[i] = 0


visit(0)