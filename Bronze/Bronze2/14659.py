from sys import stdin

n = int(input())
mount = list(map(int, input().split()))

ans = 0
count = 0
max_m = 0

for m in mount:
    if m > max_m:
        count = 0
        max_m = m
    else:
        count+=1
    ans = max(ans, count)

print(ans)