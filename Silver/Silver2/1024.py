n, l = map(int, input().split())

idx = 0
possible = -1
num = []

for i in range (l, 100+1):
    t = (i * (i-1) // 2)

    if (n-t) % i == 0 and (n-t)/i >= 0:
        possible = (n - t) // i
        idx = i
        break

if possible != -1:
    for i in range (idx):
        num.append(possible + i)
    print(*num)
else:
    print(-1)
            
