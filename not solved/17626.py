import sys
input = sys.stdin.readline

n = int(input())


length = int(n ** 0.5)
if int(length ** 2) == n:
    print(1)


num = [0 for i in range (length + 1)]
num[0] = 1


def dp(n):
    while n > 1:
        if int(n ** 0.5) > 1:
            num[0] += 1
            n = int(n ** 0.5)
        if int(n ** 0.5) == 1:
            num[0] += 1
            break
        
        print(n)


dp(n)

print(num[0])