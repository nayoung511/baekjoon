n, m = map(int, input().split())

num = list(map(int, input().split()))
start, end = 0, 1
sum = num[start]
count = 0
while (start < end and end <= n-1):
    if sum == m:
        count+= 1
        start += 1
        end = start + 1
    else:
        print(start, end, count)
        if sum + num[end] < m:
            end += 1
            sum += num[end]

        elif sum + num[end] > m:
            start+=1
            end = start + 1

        elif sum + num[end] == m:
            count += 1
            start += 1
            end = start + 1
    sum = num[start]
    #print(start, end)

print(count)