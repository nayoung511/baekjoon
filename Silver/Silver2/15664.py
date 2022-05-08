n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
num =[]

def dfs(k):
    if len(num) == m:
        print(*num)
        return
    used = 0
    for i in range (k, n):
        if used != a[i]:
            num.append(a[i])
            dfs(i+1)
            used = num.pop()

dfs(0)