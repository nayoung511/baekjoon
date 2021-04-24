n = int(input())

num = set(1, 5, 10, 50)
a = [0]
b = set()

for i in range (n):
    for j in range (len(num)):
        if a[i] + num[i]