n = input()
n = int(n)

num = [0] * 1000001
num[1] = 1
num[2] = 2

for i in range (3, n+1):
    num[i] = (num[i-1] + num[i-2]) % 15746

print(num[n])