n, m = map(int, input().split())

num = list(map(int, input().split()))

start, end = 0, 1
sum = num[start]
count = 0

if len(num) == 1:
    if num[0] == m:
        count = 1
    else:
        count = 0

else:
    while (end < n):
        if sum + num[end] == m or sum == m:
            count += 1
            start += 1
            end = start + 1
            sum = num[start]
        # sum < m
        elif sum + num[end] < m:
            # end += 1
            sum += num[end]
            end += 1
        # num[start] + num[end] >= m
        elif sum + num[end] > m or num[start] == m:
            if end == n-1 and num[end] == m:
                count += 1
                break
            # start += 1
            # end = start + 1
            else:
                start += 1
                end = start + 1
                sum = num[start]

print(count)
