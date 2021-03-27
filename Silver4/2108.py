from collections import Counter

def main():
    n = int(input())
    a = []
    sum = 0

    for i in range(n):
        c = int(input())
        sum = sum + c
        a.append(c)

    a.sort()
    #1. 산술평균
    print(sum // n)

    #2. 중앙값
    mid = n//2
    print(a[mid])
    
    #3. 최빈값
    b = Counter(a).most_common()
    if len(b) > 1:
        print(b[1][0])
    else:
        print(b[0][0])


    #4. 범위
    print(a[len(a)-1] - a[0])

main()