def factorial(n, arr, num):
    if n == 0:
        return 1

    else:
        num[n] = factorial(n-1 ,arr, num) * arr[n]
    return num[n]
    

n, m = map(int, input().split())
arr = [i+1 for i in range (n)]
num = [0] * (n+1)

factorial(n-1, arr, num)
print(num[n-1] // (num[m-1] * num[n-m-1]))
#  nCm = n! / n!(n-m)!