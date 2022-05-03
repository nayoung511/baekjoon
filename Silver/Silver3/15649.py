n, m = map(int, input().split())
arr = [0 for i in range (n+1)]
isused = [0 for i in range (n+1)]

def visit(k):
    if k == m:
        for i in range (m):
            print(arr[i], end=' ')
        print()


    for i in range (1, n+1):
        if (isused[i] == 0):
            arr[k] = i
            isused[i] = 1
            visit(k+1)
            isused[i] = 0


visit(0)
