def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return n*fac(n-1)

s = int(input())
s = fac(s)

count = 0
for i in range (len(str(s))-1):
    if s % pow(10, i+1) == 0:
        count+=1
    else:
        break

print(count)