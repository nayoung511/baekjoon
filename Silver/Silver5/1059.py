import sys
input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
s.sort()
n = int(input())

count = 0
for i in range (l-1):
    if s[i] == n:
        break
    elif s[i] < n and s[i+1] > n:
        count = (n - s[i]) * (s[i+1] - n) - 1
        break

print(count)