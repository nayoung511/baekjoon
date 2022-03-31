from sys import stdin
from collections import deque

def check90(i, j):
    if i >= j * 0.9:
        return True
    else:
        return False

n = int(input())
num = list(map(int, stdin.readline().split()))
q = deque()

for i in range (n):
    q.append(num[i])

print(q)



