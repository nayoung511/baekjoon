from collections import deque
from sys import stdin

q = deque([])

n = int(input())

for i in range (n):
    inst = stdin.readline().rstrip().split()

    if inst[0] == 'push_front':
        q.appendleft(inst[1])

    if inst[0] == 'push_back':
        q.append(inst[1])

    if inst[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else: 
            a = q.popleft()
            print(a)
    
    if inst[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else: 
            a = q.pop()
            print(a)

    if inst[0] == 'size':
        print(len(q))

    if inst[0] == 'empty':
        if len(q) == 0:
            print(1)
        else: print(0)

    if inst[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            a = q.popleft()
            print(a)
            q.appendleft(a)

    if inst[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            a = q.pop()
            print(a)
            q.append(a)
