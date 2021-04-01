from queue import PriorityQueue
from sys import stdin
n = int(input())

#문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지 나타내는 정수


for i in range (n):
    a = PriorityQueue()

    m, k = input().split()
    m = int(m)
    k = int(k)

    b = stdin.readline()

    for i in range (m):
        a.put(b[i], i)


print(a)