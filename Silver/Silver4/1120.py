a, b = map(str, input().split())

a = list(a)
b = list(b)

length = len(b)

count = 0
if len(a) == len(b):
    for i in range (length):
        if a[i] != b[i]:
            count += 1

else:
    for i in range (length):
        a.appendleft(b[i])
print(count)