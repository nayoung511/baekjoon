from sys import stdin

def prime(n):
    lst = [True] * (n)

    m = int(n ** 0.5)
    for i in range (2, m+1):
        if lst[i] == True:
            for j in range (i+i, n, i):
                lst[j] = False
    return [i for i in range (2, n) if lst[i] == True]

num = []
while(True):
    i = int(stdin.readline())
    if i == 0:
        break
    num.append(i)

print(prime(26), prime(13))
for i in range (len(num)):
    # n 보다 크고 2n 보다 작거나 같은 소수의 개수 
    if num[i] == 1:
        print(1)

    elif num[i] == 2:
        print(1)

    else:
        # 본인이 소수인 경우이상을 구해야 함 
        print(len(prime(num[i] * 2)) - len((prime(num[i] +1))))

