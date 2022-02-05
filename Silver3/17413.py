from sys import stdin
from collections import deque

d = deque()
s = list(stdin.readline().rstrip())

for i in range (len(s)):
    d.append(s[i])

print(d)