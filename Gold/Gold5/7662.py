import sys
import heapq


input = sys.stdin.readline
n = int(input())

def PriorityHeap(t):
    min_heap=[]
    max_heap=[]
    visited=[False] * 1000000

    for i in range (t):
        c, num = map(str, input().split())
        if c == 'I':
            # min, max에 원소를 넣어준다
            heapq.heappush(max_heap, (-1 * int(num), i))
            heapq.heappush(min_heap,(int(num), i))
            # 방문 처리 해준다
            visited[i] = True

        if c == 'D':
            if num == '1':
                while max_heap and visited[max_heap[0][1]] == False:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif num == '-1':
                while min_heap and visited[min_heap[0][1]] == False:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 비어있지 않다면

    if True not in visited:
        print("EMPTY")

    else:
        while max_heap and visited[max_heap[0][1]] == False:
            heapq.heappop(max_heap)
        while min_heap and visited[min_heap[0][1]] == False:
            heapq.heappop(min_heap)

        print(-1 * max_heap[0][0], min_heap[0][0])

for _ in range (n):
    t = int(input())
    PriorityHeap(t)
