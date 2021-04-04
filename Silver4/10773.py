from collections import deque
from sys import stdin

k = int(input())
q = deque([])
sum = 0

for i in range (k):
    c = stdin.readline().strip('\n')

    if c == '0':
        q.pop()
    else:
        q.append(int(c))

if len(q) == 0:
    print(0)
else:
    for i in range (len(q)):
        sum += q[i]

    print(sum)