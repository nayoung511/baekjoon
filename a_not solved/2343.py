import sys
input = sys.stdin.readline

def possibleToDivide(n, m, lecture, mid):
    count = 0
    summ = [0 for i in range (m)]
    for i in reversed (range(n)):
        if (summ[count] + lecture[i]) < mid:
            summ[count] += lecture[i]
        else:
            if count < m-1:
                count += 1
                summ[count] += lecture[i]
            else:
                break

    print(mid, summ)

    if count > m:
        return -1
    if count < m:
        return 1
    return True

def binarySearch(n, m, lecture, start, end):
    while end >= start:
        mid = (end + start) // 2
        
        if possibleToDivide(n, m, lecture, mid) == 1:
            start = mid + 1
        if possibleToDivide(n, m, lecture, mid) == -1:
            end = mid - 1

    


n, m = map(int, input().split())
lecture = list(map(int, input().split()))

print(binarySearch(n, m, lecture, 0, sum(lecture)))

