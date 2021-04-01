def pSort(a, target):
    count = 0
    for i in range (a.qsize()):
        b = a.get()
        print(b[1], target)
        if b[1] > target:
            a.get()
            count += 1
        if b[1] == target:
            count +=1
            break
        else:
            c = a.get()
            a.put(c)
            print("queue:",a.queue)
            count +=1
        print("count", count)

    return count


#s3 - 프린터 큐
from queue import PriorityQueue
from sys import stdin
n = int(input())

#문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지 나타내는 정수

for i in range (n):
    a = PriorityQueue()

    m, k = input().split()
    m = int(m)
    k = int(k)

    print("\n----------------------------")
    b = stdin.readline().split(' ')

    for i in range (m):
        a.put([int(b[i]), i])
    print(a.queue)

    for i in range (m):
        ans = pSort(a, k)
        print(ans)

print(a.queue)