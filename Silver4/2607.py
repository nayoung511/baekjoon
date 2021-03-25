from collections import Counter

def diff(a, b):
    a = Counter(a)
    b = Counter(b)
    c = a - b

    return len(list(c.elements()))

def main():
    c = int(input())
    a = []
    d = [False] * c

    for i in range(c):
        b = list(input())
        b.sort()
        a.append(b)

    first = a[0]
    for i in range(1, c):
        #같거나
        if a[i] == first:
            d[i] = True
        #한 문자 차이
        elif len(a[i]) > len(first):
            if diff(a[i], first) == 1:
                d[i] = True
        else:
            if diff(first, a[i]) == 1:
                d[i] = True

    count = 0
    for i in range (c):
        if d[i] == True:
            count +=1

    print(count)


main()