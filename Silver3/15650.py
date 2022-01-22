n, m = input().split()
n = int(n)
m = int(m)

visit = [False] * n # 이미 뽑혔는지 확인 
arr = [0] * n # 숫자를 담을 리스트

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
def solve(d):
    if d == m:
        for i in range (m):
            print(arr[i], end=' ')
        print()

    for i in range(1, n+1):
        if(visit[i] == False):
            arr[d] = i
            visit[i] = True    # already visited
            solve(d+1)      # 한 칸 위로 올라가기
            visit[i] = False    # not yet visited
    
    print(arr)

def main():
    solve(0)
