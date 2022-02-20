def pado(n):
    num = [0] * (n+1)

    if n < 3:
        return 1

    else:
        num[0] = 1
        num[1] = 1
        num[2] = 1
        
        for i in range (3, n):
            num[i] = num[i-2] + num[i-3]

        return num[n-1]

n = int(input())

for _ in range (n):
    test = int(input())

    print(pado(test))
