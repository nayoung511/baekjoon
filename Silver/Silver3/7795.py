# A가 B보다 큰 쌍의 개수
import sys
input = sys.stdin.readline

t = int(input())


for _ in range (t):
    summ = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()

    p = 0
    count = 0
    remain = 0
    # a의 원소를 확인한다
    for i in range (n):
        while True:
            #print(a[i], "count", count)
            if p == m and i != n-1:
                count += m
                break

            if p == m and i == n-1:
                break

            if a[i] <= b[p]:
                count+= p
                break

            elif a[i] > b[p]:
                count+= 1+p
                #print(a[i], "is bigger than", b[p], "count", count)
                remain = b[p]
                p += 1

                if i == n-1:
                    break
                
                

    print(count)
                






