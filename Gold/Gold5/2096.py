import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for i in range (n)]
maxx = [[0 for i in range (n)] for i in range (n+1)]

for i in range (1):
    for j in range (n):
        maxx[i][j] = graph[i][j]
minn = [[0 for i in range (n)] for i in range (n+1)]

def dpMaxx(row):
    print("hi")
    # 현재 row에 나와있는 값들과 expected value 구하기
    for i in range (n):
        if i == 0 or i == n-1:
            if i == 0:
                maxx[row][i] = max(
                    graph[row][i] + graph[row+1][i],
                    graph[row][i] + graph[row+1][i+1])
            else:
                maxx[row][i] = max(
                    graph[row][i] + graph[row+1][i],
                    graph[row][i] + graph[row+1][i-1])


        # 가장자리에 있는 값이 아니면 3개 구해야 됨
        else:
            maxx[row][i] = max(
                graph[row][i] + graph[row+1][i],
                graph[row][i] + graph[row+1][i+1],
                graph[row][i] + graph[row+1][i-1])
            
    if row < n-2:
        dpMaxx(row+1)

dpMaxx(0)
print(maxx)