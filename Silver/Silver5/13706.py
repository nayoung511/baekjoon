n = int(input())

start = 0
end = n

while end >= start:
    mid = (end+start) // 2

    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)