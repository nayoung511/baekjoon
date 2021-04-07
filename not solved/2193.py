zero = [0] * 91
one = [0] * 91

def zerodp(n):
    if n == 1: return 0
    if n == 2: return 1
    if n == 3: return 1
    if zero[n] != 0: return zero[n]
    else:
        zero[n] = zerodp(n-1) * 2
    return zero[n]

def onedp(n):
    if n == 1: return 1
    if n == 2: return 0
    if n == 3: return 1
    if one[n] != 0: return a[n]
    else:
        if onedp(n-1) == 1:
            one[n] = 1
        else: one[n] = onedp(n-1) + 1
    return one[n]


n = int(input())

a = zerodp(n)
b = onedp(n)

print(a, b, a+b)



"""
n = 1
1

n = 2
10

n = 3
100
101

n = 4
1000
1010
1001

n = 5
3, 2
10000 (2)
10010 (2)
10100 (2)
10101 (1)
10001 (1)

n = 6
4 3
100000
100010
100100
101000
101010
100001
100101
101001
"""