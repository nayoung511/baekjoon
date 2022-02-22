import sys
import heapq
input = sys.stdin.readline

n = int(input())

def heapPriority(t):
    count = 0
    minhq = []
    maxhq = []
    for _ in range (t):
        inst = list(map(str, input().split()))
        if inst[0] == 'I':
            if int(inst[1]) > 0:
                heapq.heappush(maxhq, -1 * int(inst[1]))
            else:
                heapq.heappush(minhq, int(inst[1]))

        elif inst[0] == 'D':
            if inst[1] == '1':
                if len(maxhq) > 0: # delete max
                    heapq.heappop(maxhq)
                elif len(maxhq) == 0 and len(minhq) > 0:
                    heapq.heappop(minhq)

            if inst[1] == '-1':
                if len(minhq) > 0: # delete min
                    heapq.heappop(minhq)
                elif len(minhq) == 0 and len(maxhq) > 0:
                    heapq.heappop(maxhq)
        
        print(inst, maxhq, minhq)
    return minhq, maxhq

for _ in range (n):
    t = int(input())
    minhq, maxhq = heapPriority(t)
    if len(minhq) == 0  and len(maxhq) == 0:
        print("EMPTY")
    else:
        print(maxhq, minhq)
        if len(maxhq) == 0:
            print(max(minhq), min(minhq))
        elif len(minhq) == 0:
            print(max(maxhq) * -1, min(maxhq)*-1)
            
        else:    
            print(maxhq[0] * -1, minhq[0])



    # if len(minhq) == 0 or len(maxhq) == 0:
    #     print("EMPTY")
    # else:
    #     print(-1* maxhq[0], minhq[0])







    
# def dualPriority(t):
#     q = PriorityQueue()
#     temp = PriorityQueue()
#     maxx = 0
#     for _ in range (t):
#         inst = list(map(str, input().split()))
#         if inst[0] =='I':
#             q.put(inst[1])
#             if int(inst[1]) > maxx:
#                 maxx = int(inst[1])

#         if inst[0] == 'D' and q.empty() == False:
#             if inst[1] == '1': # delete max
#                 print("Max is", q.get()[-1])

#                 # back
#             else: # delete min
#                 q.get()

#         print("final q", q.queue)

#     return q, maxx

    
# for _ in range (n):
#     t = int(input())
#     q, maxx = dualPriority(t)
#     print(q.queue)

#     if q.empty():
#         print("EMPTY")

#     else:
#         print(q.get()[int(maxx)], q.get())



