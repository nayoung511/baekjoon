n, m = input().split()
n = int(n)  # 범위
m = int(m) # 뽑는 수 

visit = [False] * 10

# 1 = true
# 0 = false

arr = [0] * 10

def solve(d):
    if d == m:
        for i in range (m):
            print(arr[i], end=' ')
        print()

    for i in range(1, n+1):
        if(visit[i] == False):
            arr[d] = i
            visit[i] = 1    # already visited
            solve(d+1)      # 한 칸 위로 올라가기
            visit[i] = 0    # not yet visited
        

def main():
    solve(0)

main()