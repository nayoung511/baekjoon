import sys
input = sys.stdin.readline

n = int(input())
fluid = list(map(int, input().split()))
fluid.sort()
minn = max(fluid)

def binarySearch(start, end, idx, minn):
    lowIdx, highIdx = 0, 0
    while end >= start:
        mid = (end + start) // 2

        if abs(fluid[mid] - idx) < minn:
            minn = abs(fluid[mid] - idx)
            lowIdx = mid
            start = mid + 1
            
        else:
            end = mid - 1

    return minn, lowIdx

ans = max(fluid)
for i in range (n):
    ans, lowIdx,  = binarySearch(i+1, n-1, i, minn)
    minn = min(minn, ans)

print(minn)
