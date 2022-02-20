from sys import stdin

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


ans = ''
n, m = list(map(int, stdin.readline().split())) 

if gcd(n, m) == 1:
    print(1)
else:
    ans += '1' * (gcd(n, m))
#ans =((10 ** gcd(n, m)) -1) // 9


print(ans)
# 111 , 1111 
# = (10^3 - 1) // 9 , (10^4 -1) // 9