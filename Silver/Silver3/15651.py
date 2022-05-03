n, m = map(int, input().split())
num =[]

def dfs(cnt):
    if len(num) == m:
        print(*num)
        return
    
    for i in range (cnt, n+1):
        num.append(i)
        dfs(i)
        num.pop()

dfs(1)