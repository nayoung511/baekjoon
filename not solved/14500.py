import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tetris = [list(map(int, input().split())) for i in range (n)]

def main():
    maxx = 0
    print(tetris)
    row, col, nextrow, nextcol = 0,0,0,0

    # 일단 max를 가지는 2개를 찾아야 함
    for i in range(n-1):
        for j in range (m-1):
            # 왼쪽 
            if (tetris[i][j] + tetris[i][j+1] > maxx):
                maxx = tetris[i][j] + tetris[i][j+1]
            # 아래
            if (tetris[i][j] + tetris[i+1][j] > maxx):
                maxx = tetris[i][j] + tetris[i+1][j]


    # max 값마다 테트로미노 함수 실행
    for i in range(n-1):
        for j in range (m-1):
            # 왼쪽 
            if (tetris[i][j] + tetris[i][j+1] == maxx):
                maxx = tetris[i][j] + tetris[i][j+1]
                row, col, nextrow, nextcol = i, j, i, j+1

                print(one(maxx, row, col, nextrow, nextcol))
            # 아래
            if (tetris[i][j] + tetris[i+1][j] == maxx):
                maxx = tetris[i][j] + tetris[i+1][j]
                row, col, nextrow, nextcol = i, j, i+1, j
                print(one(maxx, row, col, nextrow, nextcol))


"""
-----------------
|   |   |   |   |
-----------------
"""
def one(maxx, row, col, nextrow, nextcol):
    summ1, summ2, summ3 = 0, 0, 0
    horiSum, vertiSum = 0, 0
    if row == nextrow:
        #오른쪽 쫘르르 3개
        if nextcol + 2 < m:
            summ1 = maxx + tetris[row][col+2] + tetris[row][col+3]
            
        #왼쪽 쫘르르 3개
        if col - 2 >= 0:
            summ2 = maxx + tetris[row][col-1] + tetris[row][col-2]

        # 왼, 오
        if nextcol + 1 < m and col - 1 > 0:
            summ3 = maxx + tetris[row][col-1] + tetris[row][nextcol+1]

        horiSum = max(summ1, summ2, summ3)

    else:
        #아래로 쫘르륵
        if nextrow + 2 < n:
            summ1 = maxx + tetris[row+2][col] + tetris[row+3][col]
        
        #위로 쫘르륵
        if row - 2 >= 0:
            summ2 = maxx + tetris[row-1][col] + tetris[row-2][col]

        #위, 아래
        if nextrow + 1 < n and row - 1 >= 0:
            summ2 = maxx + tetris[row-1][col] + tetris[nextrow+1][col]

        vertiSum = maxx(summ1, summ2, summ3)

    return max(horiSum, vertiSum)


"""
___
|__|
|__|__
|__|__|
"""
def two(maxx, row, col, nextrow, nextcol):
    if row == nextrow:
        # 왼쪽 위

        # 오른쪽 위


        # 왼쪽 아래


        # 오른쪽 아래


    else:



"""
___
|__|__
|__|__|
   |__|
"""


"""
 ------------
|___|___|___|
    |___|
"""



"""
________
|___|___|
|___|___|
"""

main()