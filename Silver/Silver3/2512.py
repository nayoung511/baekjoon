import sys
input = sys.stdin.readline

def calSum(n, arr, mid):
    summ = 0
    for i in range (n):
        if arr[i] > mid:
            summ += mid
        else:
            summ += arr[i]
    
    return summ

def binarySearch(n, arr, start, end, target):
    while end >= start:
        mid = (start + end) // 2

        if calSum(n, arr, mid) > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return end

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = int(input())


if sum(arr) < target:
    print(max(arr))

else:
    print(binarySearch(n, arr, 0, arr[-1], target))