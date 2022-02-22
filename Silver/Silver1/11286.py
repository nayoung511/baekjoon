import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())

q = PriorityQueue()
maxx = 0
for _ in range (n):
    a = int(input())
    if a != 0:
        if a > 0:
            q.put((a, True))
        else: #음수라면
            q.put((-1 * a, False))

    elif a == 0: # 배열에서 절댓값이 가장 작은 값 출력
        if q.empty():
            print(0)
        else:
            b = q.get()
            q.put(b)
            if b[1] == False:
                print((q.get()[0]) * -1)
 
            else:
                print(q.get()[0])

    #print("a:", a, q.queue)