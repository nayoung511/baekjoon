import sys
input = sys.stdin.readline

n, m = map(int, input().split())
label = []
status = []

def binarySearch(status, start, end, x):
    while end >= start:
        mid = (end + start) // 2
        if status[mid] < x:
           start = mid + 1
        else:
           end = mid - 1

    return end+1

for _ in range (n):
    a, b = map(str, input().split())
    if label and label[-1] == int(b):
        continue
    label.append(a)
    status.append(int(b))

for _ in range (m):
    a = int(input())
    print(label[binarySearch(status, 0, len(status)-1, a)])

