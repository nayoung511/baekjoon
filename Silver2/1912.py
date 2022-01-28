from sys import stdin

n = int(input())
num = list(map(int, stdin.readline().split()))
arr = [0] * (n)
arr[0] = num[0]

for i in range (1, n):
    arr[i] = max(arr[i-1] + num[i], num[i])

print(max(arr))

