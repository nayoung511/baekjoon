#양수 --> 오른쪽 append
#음수 --> 왼쪽 appendleft

from collections import deque
from sys import stdin

n = int(input())
q = deque([])
ans = []
balloon = stdin.readline().split()

for i in range (n):
    q.append([int(balloon[i]), i+1])

#first ballon
idx = q.popleft()
ans.append(idx[1])

for i in range (n-1):
    if idx[0] > 0:
        for j in range (idx[0]-1):
            a = q.popleft()
            q.append(a)
        idx = q.popleft()
        q.appendleft(idx)

    else:
        for j in range (abs(idx[0])):
            a = q.pop()
            q.appendleft(a)
        idx = q.pop()
        q.append(idx)

    idx = q.popleft()
    ans.append(idx[1])
    
for i in ans:
    print(i, end =" ")
    

