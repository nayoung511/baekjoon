import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

"""
    0     n//2    n
    ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    |      |      |
    |   1  |  2   |
     ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 
    |      |      |
    |   3  |   4  |
    ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

"""
  # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
  # 4등분 한다

def traverseZ (n, r, c, count):
  # until 2 row 2 col 일 때까지 divide 한다
    if n <= 2:
        if r==0 and c==0:
            count = count
        if r==0 and c==1:
            count += 1
        if r==1 and c==0:
            count += 2
        if r==1 and c==1:
            count += 3


    else:
        m = n//2
        # 1
        if r < m and c < m:
            count = traverseZ(m, r, c, count)
    
        # 2
        if r < m and c >= m:
            #1 사분면 traverse 횟수 더해줘야됨
            acc_count = (count + (m*m))
            count = traverseZ(m, r, c-m, acc_count)
        
        # 3
        if r >= m and c < m:
            # 1,2 사분면 traverse 횟수 더해줘야됨
            acc_count = (count + (m * m)*2 )
            count = traverseZ(m, r-m, c, acc_count)

        # 4
        if r >= m and c >= m:
            #1, 2, 3사분면 traverse횟수 더해줘야됨
            acc_count = (count + (m*m)* 3)
            count = traverseZ(m, r-m, c-m, acc_count)


    return count
        


print(traverseZ((2**n), r, c, 0))