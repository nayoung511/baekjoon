import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

color = [list(map(str, input().rstrip())) for _ in range (n)]
visited = [[0 for i in range (n)]for j in range (n)]

print(color)
print(visited)
countBlue = 0
countRed = 0
countGreen = 0

def nonColorBlind(x, y):
    global countRed
    q = deque([])
    q.append((x, y)) 
    countRed += 1
    print(countRed)

    while q:
        print(q)
        ex, ey = q.popleft()

        for i in range (4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if (0<= nx < n-1 and 0<= ny < n-1):
                if (visited[nx][ny] == 0):
                    # red
                    if (color[nx][ny] == 'R'):
                        visited[nx][ny] = countRed
                        q.append((nx, ny))
    
    
   

                    #  red


                    # green
        

for i in range (n):
    for j in range (n):
        if color[i][j] == 'R':      
            print("found!")
            nonColorBlind(i, j)
            

#nonColorBlind(0,0)
countRed += 1
print(countRed)

print(visited)

print(countRed)


# def ColorBlind():
#     return count

