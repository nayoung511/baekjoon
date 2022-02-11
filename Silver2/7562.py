from collections import deque

n = int(input())

#한번에 한방향 +-2, 다른 방향 +- 1
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y):

    # 큐에 원소를 집어 넣고, 
    q = deque([[x, y]])
    # 큐에 있는 원소를 하나씩 pop하면서
    while q:
        ex, ey = q.popleft()

        if ex == n and ey == m:
            return board[ex][ey]

        # check NEWS
        for k in range (8):
            nx = ex + dx[k]
            ny = ey + dy[k]

            # check if they are in range
            if 0<=nx<size and 0<=ny<size:
                if check[nx][ny] == False:
                    check[nx][ny] = True

                    board[nx][ny] = board[ex][ey] + 1
                    q.append([nx, ny])



for _ in range (n):
    board=[]
    # size of chess board
    size = int(input())

    board = [[0] * (size) for _ in range (size)]
    check = [[False] * (size) for _ in range (size)]
    # 현재 칸
    a, b = map(int, input().split())
    # 이동하려는 칸 
    n, m = map(int, input().split())

    print(bfs(a, b))