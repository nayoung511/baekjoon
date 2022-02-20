import sys
from queue import PriorityQueue
input = sys.stdin.readline

q = PriorityQueue()

n = int(input())

for _ in range (n):
    inp = int(input())

    if inp == 0:
        if q.empty():
            print(0)
        else:
            print(q.get()[1])

    else:
        q.put((-inp, inp))

    