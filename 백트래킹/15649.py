n, m = input().split()
n = int(n)
m = int(m)

visit = [False] * 10
arr = [0] * 10

def solve(d):
    if d == m:
        for i in range (m):
            print(arr[i], end=' ')
        print()

    for i in range(1, n+1):
        if(visit[i] == False):
            arr[d] = i
            visit[i] = 1
            solve(d+1)
            visit[i] = 0
        

def main():
    solve(0)

main()