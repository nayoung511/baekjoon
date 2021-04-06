import sys
sys.setrecursionlimit(10**6)

"""
입력 정답 출력
321   9  10
609  10  11
642  10  11
643  11  12
645  11  12
963  10  11
"""
a = [] * (10**6) + 1

def dp(n):
    if n % 3 == 0: n = n // 3
    if n % 2 == 0: n = n // 2

    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 1
    
    else:
        n = n - 1

    return 

    
    


n = int(input())
