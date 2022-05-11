a = int(input())

num = [1 for i in range (30)]

def combination(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n * combination(n-1)

for i in range (1, 30):
    num[i] = combination(i)

for _ in range (a):
    n, m = map(int, input().split())
    print(num[m] // (num[m-n] * num[n]))