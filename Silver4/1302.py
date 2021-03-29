from collections import Counter
from sys import stdin

def main():
    c = int(input())
    a = []
    
    for i in range (c):
        d = stdin.readline()
        a.append(d.strip('\n'))

    a = Counter(a)
    print(a)
    b = a.most_common()
    print(b, b[0][1])
    c = a.most_common(b[0][1])
    print(a.most_common(1))
    print(c)


    if len(c) > 1:
        c.sort()
        print(c[0][0])
    else:
        print(c[0][0])


main()