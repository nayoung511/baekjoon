from collections import deque
from sys import stdin

def main():
    q = deque([])
    c = int(input())

    for i in range(c):
        inst = stdin.readline().split()

        if inst[0] == 'push':
            q.append(inst[1])
        
        if inst[0] == 'top':
            if len(q) == 0:
                print(-1)
            else:
                a = q.pop()
                print(a)
                q.append(a)
        
        if inst[0] == 'pop':
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
            else:
                print(0)
        
main()
