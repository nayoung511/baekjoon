import sys
input = sys.stdin.readline

# pypy3
# 기본 가정: 같은 행에는 퀸을 놓지 않는다
def n_queens(n):
    if n == N:
        global count
        count += 1
    else:
        for i in range (N):
            if visited[i]:
                continue
            
            board[n] = i
        
            if promising(n):
                visited[i] = True
                n_queens(n+1)
                visited[i] = False
            

def promising(n):
    #같은 열이나 같은 대각선에 놓이는지 확인
    for i in range (n):
        if (board[n] == board[i] or (abs(board[n] - board[i]) == (n-i))):
            return False
    
    return True

if __name__=='__main__':
    N = int(input())
    count = 0
    board = [0 for _ in range (N)]
    visited = [False for _ in range (N)]
    
    n_queens(0)
    print(count)
