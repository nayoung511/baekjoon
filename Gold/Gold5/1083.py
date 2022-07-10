import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

move = 0
swap = 0
while (move < s and swap < n-1):
    maxx = arr[swap]
    maxIdx = -1

    idx = swap + 1
    count = 1
    while (move + count <= s and idx < n):
        num = arr[idx]
        if (num > maxx):
            maxx = num
            maxIdx = idx

        count += 1
        idx += 1
    if maxIdx != -1:
        arr.remove(arr[maxIdx])
        arr.insert(swap, maxx)
        move += maxIdx - swap
    
    swap+=1


print(*arr)
