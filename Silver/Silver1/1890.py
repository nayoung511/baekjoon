import sys
input = sys.stdin.readline

n = int(input())
num = [list(map(int, input().split())) for i in range (n)]
dp = [[1 for _ in range (n)] for _ in range (n)]

counter = 1
def move(x, y):
    global counter
    nx = 1 * num[x][y]
    ny = 1 * num[x][y]

    print(nx, ny)

    if 0<=nx<n and 0<=ny<n:
        dp[nx][y] += counter
        dp[x][ny] += counter
        counter+=1

        for i in range (n):
            print(dp[i])

        move(nx, y)
        move(x, ny)

        # if dp[n-1][n-1] != 1:
        #     return

        # else:
        #     move(nx, y)
        #     move(x, ny)

move(0, 0)
print()
print(dp)


