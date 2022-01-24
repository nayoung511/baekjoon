def solve(d):
    if visit[d] == False:
        visit[d] == True
        arr[d][0] = d

    for i in range (d+1, m):
        if visit[i] == False:
            arr[d][i] = i



n, m = map(int, input().split())

visit = [False] * (n+1) # 이미 뽑혔는지 확인 
arr = [[0 for i in range (m)] for i in range (n+1)] # 숫자를 담을 리스트

for i in range (1, n+1):
    solve(i)

print(arr)