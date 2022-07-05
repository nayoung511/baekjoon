import sys
input = sys.stdin.readline

"""
e.g
13 10 12 11 10 11 12
# 1. 먼저 sort
10 10 11 11 12 12 13

# 2. 양 끝에 min을 배치
10 11 12 13 12 11 10

# 3. 높이값의 최댓값 구함
"""

t = int(input())
for _ in range (t):
    n = int(input())
    # 미리 빈 배열 선언
    arr = [0 for i in range (n)]

    log = list(map(int, input().split()))
    log.sort()

    # 양 끝에 min들을 배열하는 식
    for i in range (0, n, 2):
        arr[i//2] = log[i]

    for i in range (1, n, 2):
        arr[-i // 2] = log[i]
    
    maxx_diff = 0
    for i in range (n-1):
        maxx_diff = max(maxx_diff, abs(arr[i] - arr[i+1]))

    print(maxx_diff)