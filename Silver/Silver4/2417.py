n = int(input())
start, end = 0, n

while end >= start:
    mid = (start+end) // 2
    #mid의 제곱값
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)

