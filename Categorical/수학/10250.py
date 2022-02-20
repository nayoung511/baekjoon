t = int(input())
for i in range (t):
    h, w, n = map(int, input().split())

    height = n % h
    width = (n // h)

    if n % h == 0:
        height = h
    else:
        width += 1

    if width < 10:
        print(height, 0, width, sep='')
    else:
        print(height, width, sep='')
    

"""
2
6 12 10 = 402

10 % 6 = 4
10 // 6

30 50 72 = 1203
72 % 30
72 // 30

"""