n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
num =[]

def dfs(k):
    if len(num) == m:
        print(*num)
        return
    
    for i in range (k, n):
        num.append(a[i])
        dfs(i)
        num.pop()

dfs(0)