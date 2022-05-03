n, m = map(int, input().split())
num =[]

def dfs(cnt):
    if len(num) == m:
        print(*num)
        return
    
    for i in range (n):
        num.append(i+1)
        dfs(i+1)
        num.pop()

dfs(1)
