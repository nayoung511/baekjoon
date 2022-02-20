def Euclidean (a, b):
    r = b % a
    if r == 0:
        return a
    return Euclidean(r, a)

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

# 분모가 같을 때
if d1 == d2:
    d3 = d1
    n3 = n1 + n2
    
else:
    d3 = d1 * d2
    n3 = (n1 * d2) + (n2 * d1)


# 기약 분수인지 확인 
val = Euclidean(n3, d3)

if val == 1:
    print(n3, d3, sep=' ')

else:
    n3 = n3 // val
    d3 = d3 // val
    print(n3, d3, sep=' ')