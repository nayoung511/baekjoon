def main():
    s1, e1 = input().split()
    x, y = input().split()

    s1 = int(s1)
    e1 = int(e1)
    x = int(x)
    y = int(y)

    s = (s1-y) / x
    e = (e1-y) / x

    p = int(e - s)

    lst = set()

    for i in range (0, p+1):
        c = (i * x) + y
        if (c <= e1) and (c >= s1):
            lst.add(c)

    if len(lst) > 1:
        print("Unknwon Number")
    else:
        str1 = ''
        lst = list(lst)
        a = str1.join(map(str, lst))
        print(a)
        
main()