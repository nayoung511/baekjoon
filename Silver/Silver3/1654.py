#가지고 있는 랜선의 개수 k
#필요한 랜선의 개수 n

def binaryS(a, target, h, l):
    while h>= l:
        temp = 0
        mid = (h+l) // 2
        for i in range (len(a)):
            temp += a[i] // mid

        if target > temp:
            h = mid - 1

        if target <= temp:
            l = mid +1

    return h

k, n = input().split()
k = int(k)
n = int(n)
ans = 0
a = []

for i in range (k):
    s = int(input())
    a.append(s)

high = sum(a) // n #1~h사이에 답
low = 1
print(binaryS(a, n, high, low))




