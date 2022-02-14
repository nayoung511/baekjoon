# 가장 긴 증가하는 부분 수열
# 수열의 크기 N = 1,000,000

import sys
input = sys.stdin.readline

def binarySearch(item):
    start = 1
    end = len(dp)-1
    while end > start:
        mid = (start + end) // 2

        if dp[mid] < item:
            start = mid+1
        elif dp[mid] > item:
            end = mid
        else:
            start = end = mid

    return end

n = int(input())
num = list(map(int, input().split()))

# 정답 수열이 들어갈 배열
# 처음 값은 나올 수 없는 가장 작은 값 = 0
dp=[0]

for item in num:
    endOfdp=dp[-1]

    # 만약 수열의 값이 현재 dp에 들어 있는 값보다 크다면
    if item > endOfdp:
        # dp배열에 넣어준다
        dp.append(item)

    else:
        # 작다면 lower bound를 찾아 갱신해준다
        dp[binarySearch(item)] = item
print(len(dp)-1)