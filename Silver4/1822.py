def Bsearch(a, target, h, l):
    while h >= l:
        mid = (h+l)//2
        if a[mid] == target:
            return True
        elif a[mid] > target:
            return Bsearch(a, target, mid-1, l)
        else:
            return Bsearch(a, target, h, mid+1)
    return False

def main():
    n, m = input().split()

    n = int(n)
    m = int(m)

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    l = []

    #집합 A에는 속하면서 집합 B에는 속하지 않는 원소의 개수
    for i in range (len(a)):
        #print(a[i])
        ans = Bsearch(b, a[i], len(b)-1, 0)

        if ans == False:
            l.append(a[i])

    print(len(l))
    i = ' '.join(map(str, l))
    print(i)


main()