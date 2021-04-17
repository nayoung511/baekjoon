"""
자신보다 낮은 봉우리에 서 있는 적만 처치할 수 있다
"""
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