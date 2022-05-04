n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
num =[]

def dfs(cnt):
    if len(num) == m:
        print(*num)
        return
    
    for i in range (cnt, n):
        if arr[i] not in num:
            num.append(arr[i])
            dfs(i+1)
            num.pop()

dfs(0)