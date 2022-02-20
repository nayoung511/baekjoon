c = int(input())
a = [0] * (c+1)
a[1] = 1

for i in range(2, c+1):
    a[i] = a[i-1] + a[i-2]

print(a[-1])