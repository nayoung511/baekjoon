from collections import Counter
from sys import stdin

def main():
    n = int(input())
    a = []
    name = []
    
    for i in range (n):
        d = stdin.readline().rstrip()
        a.append(d)

    a = Counter(a)
    b = a.most_common()
    c = [list(i) for i in b]
    max = c[0][1]

    for i in range (len(c)):
        if c[i][1] == max:
            name.append(c[i][0])

    name.sort()

    if (len(c)) > 1:
        print(name[0])
    else:
        print(name[0])

main()