import sys
input = sys.stdin.readline

n = int(input())

num = [float(input()) for _ in range (n)]

for i in range (1, n):
    num[i] = max(num[i-1] * num[i], num[i])

print("{:.3f}".format(max(num)))