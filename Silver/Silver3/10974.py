n = int(input())
arr = []

def dfs(k):
    if k == n:
        print(*arr)
        return

    for i in range (1, n+1):
        if i not in arr:
            arr.append(i)
            dfs(k+1)
            arr.pop()

dfs(0)
