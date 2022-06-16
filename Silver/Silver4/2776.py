import sys
input = sys.stdin.readline

t = int(input())

def binarySearch(noteOne, low, high, x):
    while high >= low:
        mid = (high + low) // 2

        # 발견했다면
        if noteOne[mid] == x:
            return 1

        elif noteOne[mid] > x:
            high = mid - 1

        else:
            low = mid+1
    return 0

# 수첩2에 적혀있는 M개의 숫자 순서대로, 수첩1에 있으면 1을 없으면 0을 출력
for _ in range (t):
    n = int(input())
    noteOne = list(map(int, input().split()))
    noteOne.sort()

    m = int(input())
    noteTwo = list(map(int, input().split()))

    for i in range (m):
        print(binarySearch(noteOne, 0, n-1, noteTwo[i]))