def Bsearch(a, target, l, h):
    while l <= h:
        mid = (l + h) // 2
        if a[mid] == target:
            return 1
        elif (a[mid] > target):
            return Bsearch(a, target, l, mid -1)
        else:
            return Bsearch(a, target, mid+1, h)
    return 0

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    m = int(input())
    b = list(map(int, input().split()))

    d = []

    for i in range (m):
        c = Bsearch(a, b[i], 0, len(a)-1)
        d.append(c)

    e = ' '.join(map(str, d))

    print(e)




main()