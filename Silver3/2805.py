def binary_height(arr, mid, m):
    sum = 0
    for i in arr:
        if i >= mid:
            sum += i - mid

    if sum >= m:
        return True
    else:
        return False


n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 1
max_height = 0
for i in height:
    if i >= max_height:
        max_height = i
end = max_height

# array 전체를 검사 
while (start <= end):
    mid = (start + end) // 2

    value = binary_height(height, mid, m)
         
    if value == True:
        start = mid + 1
    else:
        end = mid - 1

print(mid, start, end)
