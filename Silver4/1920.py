def Bsearch(a, target, l, h):
    #print("hi")
    while l <= h:
        mid = (l+ h) // 2
        #print(a[mid], target)
        if a[mid] == target:
            return 1
        elif (a[mid] > target):
            h = mid -1
        else:
            l = mid+1
    return 0


def main():
    n = int(input())
    inp = list(map(int, input().split()))
    inp.sort()
    
    lst = [0] * n

    m = int(input())
    out = list(map(int, input().split()))
    
    print("-------------------------------------")
    for i in range (n):
        a = Bsearch(out, inp[i], 0, len(out)-1)
        print(a)


main()