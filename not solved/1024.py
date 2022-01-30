def check (m, a, l):
    sum = 0
    arr = [] # 정답 담을 리스트
    #길이 l의 sum check 
    for i in range (l):
        sum += a[m-i]
        arr.append(a[m-i])

    # sum > n

    # sum < n

    # sum == n
    if sum == n:
        return m



n, l = map(int, input().split())

a = [i for i in range (1, n+1)]

m = (n-1) // 2 - 1

for i in range (l+1, 0, -1):
    print(a[m-i])
    count += a[m-i]

print(count)
