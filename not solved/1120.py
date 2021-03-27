def checkDiff(a, b):
    c = []
    for i in range (len(a)):
        if a[i] != b[i]:
            c.append(i)
    return len(i)

def strify(a):
    return ''.join(map(str, a))

def main():
    #len(A) <= len(B)

    a, b = input().split()
    a = list(a)
    b = list(b)
    c = []

    print("--------------------------------------")
    print(strify(a))
    print(strify(b))

    for i in range(len(a)):
        if a[i] != b[i]:
            c.append(' ')
        else:
            c.append(a[i])

    print(c)

    a_mid = len(a) // 2
    print(a_mid)

    for i in range (len(b) - len(a)):
        #앞에 추가
        if a[i] != b[i]:
            a.insert(0, b[i])
        else:
            a.append(b[len(b)-1])

    print(strify(a), strify(b))

    c = []
    for i in range (len(b)):
        #print(a[i], b[i])
        if a[i] != b[i]:
            c.append(i)

    print(c)

    print(strify(a), strify(b))

    

main()