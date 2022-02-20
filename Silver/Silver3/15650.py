n, m = map(int, input().split())
num =[]

def dfs(cnt):
    if len(num) == m:
        print(*num)
        return
    
    for i in range (cnt, n+1):
        if i not in num:
            num.append(i)
            dfs(i+1)
            num.pop()

dfs(1)