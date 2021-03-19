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
    inp = list(map(int, input().split()))
    inp.sort()

    m = int(input())
    out = list(map(int, input().split()))

    for i in range (m):
        a = Bsearch(inp, out[i], 0, len(inp)-1)
        print(a)



main()