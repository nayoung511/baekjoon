from sys import stdin

def sipja(num):
    a = [num]
    for i in range (1, 4):
        print(num[1:], num[0:1])
        num = num[1:] + num[0:1]
        a.append(num)
    return min(a)
        
n = input().split(" ")

n = sipja(n)
count = 0
for i in range (1111, n):
    if sipja(i) == n:
        count+=1

print(count)
