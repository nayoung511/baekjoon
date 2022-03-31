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
    if n == 2: 
        x[n] = 1
        return x[n]
    if n == 3:
        x[n] = 1
        return x[n]
    if n == 5:
        x[n] = 1
        return x[n]
    if n == 7:
        x[n] = 1
        return x[n]
    if x[n] != 0: return x[n]
    else:
        if n % 2 == 0:
            x[n] = nFac(n//2) + 1
        else:
            x[n] = nFac(n // 2)
    return x[n]
    
#소수만 판별
prime_b = prime_list(b)

for i in range (a, b+1):
    nFac(i)

print(x[a:b])
count = 0

for j in range (a, b+1):
    i = x[j]
    if  i!= 0 and i != 1 and i % 2 != 0:
        count += 1
    if i == 2:
        count +=1
print(count)
