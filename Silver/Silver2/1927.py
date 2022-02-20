from queue import PriorityQueue
import sys

input=sys.stdin.readline
n = int(input())
num = PriorityQueue()
for i in range (n):
    inp = int(input())

    if inp == 0:
        if num.empty():
            print(0)
        else:
            print(num.get())
            #num.pop
    else:
        num.put(inp)
