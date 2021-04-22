# 연속해서 커지거나, 연속해서 작아지는 (같은 것 포함)
from sys import stdin
n = int(input())

a = stdin.readline().split()

max_l = 1
current_l = 1
for i in range (n-1):
    #increasing
    if a[i] >= a[i+1]:
        current_l += 1
    else:
        current_l = 1
    max_l = max(current_l, max_l)

current_l = 1
for i in range (n-1):
    #decreasing
    if a[i] <= a[i+1]:
        current_l += 1
    else:
        current_l = 1
    max_l = max(current_l, max_l)

print(max_l)
