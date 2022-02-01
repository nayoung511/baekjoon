def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

a, b = map(int, input().split())

# a 와 b의 최소공배수를 한 줄에 입력 
gcd_val = gcd(b, a)

print((a * b) // gcd_val)


