def Bsearch(a, target, h, l):
    while l <= h:
        mid = (h + l) // 2
        if a[mid] == target:
            return True
        elif a[mid] > target:
            return Bsearch(a, target, mid -1, l)
        else:
            return Bsearch(a, target, h, mid+1)
    return False

def main():
    n,m = input().split()
    n = int(n)
    m = int(m)

    hear = []  # 듣도 못한 사람 
    see = []   # 보도 못한 사람
    com = []   # 듣보잡

    for i in range (n):
        name = input()
        hear.append(name)

    for i in range (m):
        name = input()
        see.append(name)

    hear.sort()
    see.sort()

    #hear과 see의 공통
    for i in range (m):
        a = Bsearch(hear, see[i], len(hear)-1, 0)
        if a == True:
            com.append(see[i])

    com.sort()
    print(len(com))
    for name in com:
        print(name)


main()