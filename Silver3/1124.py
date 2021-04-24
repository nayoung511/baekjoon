a, b = map(int, input().split())
x=[0]*(b+1)

#에라토스테네스의 체
def prime_list(n):
    s = [True] * n

    m = int(n ** 0.5)
    for i in range (2, m+1):
        if s[i] == True:
            for j in range (i+i,n,i):
                s[j] = False
    return [i for i in range (2, n) if s[i] == True]


def nFac(n):
    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 1
    if n == 5: return 1
    if n == 7: return 1
    if x[n] != 0: return x[n]
    else:
        x[n] = nFac(n//2) + 1
    return x[n]

    
    
#소수만 판별
prime_b = prime_list(b)
prime = [i for i in prime_list(b) if i not in prime_list(a)]

nFac(b)
print(x)


