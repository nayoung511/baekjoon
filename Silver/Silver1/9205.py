import sys
input = sys.stdin.readline

# 맥주 한 박스: 맥주 20개
# 50m에 한 병씩: 가기 전에 마셔야 됨

t = int(input())
for _ in range (t):
    n = int(input()) # 편의점의 개수    
    
    graph = [[0 for i in range (2)] for i in range (n+2)]
    dist = [0 for i in range (n+1)]
    beer = [0 for i in range (n+1)]

    hx, hy = map(int, input().split())
    graph[0][0] = hx
    graph[0][1] = hy
    
    for i in range (1, n+1):
        x, y = map(int, input().split())
        graph[i][0] = x
        graph[i][1] = y
    fx, fy = map(int, input().split())
    graph[-1][0] = fx
    graph[-1][1] = fy

    flag = False
    # calculate the distance
    for i in range (n+1):
        dist[i] = (graph[i+1][1] - graph[i][1]) + (graph[i+1][0]-graph[i][0])
        if dist[i] > (20*50):
            flag = True
            break


    if flag:
        print("sad")
    else:
        print("happy")




    

