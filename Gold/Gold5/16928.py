import sys
from collections import deque
input = sys.stdin.readline

# n = 사다리의 수
# m = 뱀의 수

n, m = map(int, input().split())
board = [0 for i in range (100+1)]
move = []
# 사다리의 정보
for i in range (n):
    # x, y
    # x번 칸에 도착하면 y번 칸으로 이동
    move.append(list(map(int, input().split())))
    board[move[i][0]] = move[i][1]

# 뱀의 정보
for i in range (m):
    # u, v
    move.append(list(map(int, input().split())))
    board[move[i][0]] = move[i][1]

move.sort()

print(board)
# 100번 칸에 도착하기 위해 최소 주사위 (1~6)
start = 1
dice = [1,2,3,4,5,6]
count = 0

def lsgame(start):
    global count
    flag = False
    while start < 100:
        for i in range (len(move)):
            if start < 100:
                for j in range (len(dice)):
                    print(start, dice[j], move[i][0])
                    if start + dice[j] == move[i][0] and start + dice[j] < 100:
                        start = move[i][1]
                        count+=1

                    elif start + dice[j] == 100:
                        start += dice[j]
                        count+=1
                        print("start", start)
                        flag = True

                    elif start + dice[j] < 100:
                        # 끝까지 왔는데 지름길이 없으면
                        if i == len(dice)-1:
                            start += dice[-1]
                            count+=1
                            lsgame(start)

                    

lsgame(start)

print(count)

        