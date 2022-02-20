from collections import Counter
from sys import stdin

def main():
    n = int(input())
    a = []

    for i in range(n):
        c = stdin.readline()
        a.append(int(c))

    print(a)
    a.sort()
    #1. 산술평균
    print(round(sum(a) / n))

    #2. 중앙값
    if n % 2 == 1:
        mid = n//2
        print(a[mid])
    else:
        print((a[n//2 + 1] + a[n//2]) // 2)
    
    #3. 최빈값
    b = Counter(a).most_common()
    if len(b) > 1:
        if b[0][1] == b[1][1]:
            print(b[1][0])
    else:
        print(b[0][0])


    #4. 범위
    print(a[len(a)-1] - a[0])

main()