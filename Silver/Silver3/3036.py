def gcd(n, m):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
    

n = int(input())
ring = list(map(int, input().split()))

first = ring[0]
for i in range (1, n):
    value = gcd(first, ring[i])
    print(first // value,"/",ring[i]//value, sep='')