n = int(input())

a=[]
for i in range (n):
    i = input()
    a.append(i)

count = 1
for idx in range (len(a[0])-1, -1, -1):
    count = 0
    s = set()
    for i in range (n):
        v = a[i][idx:]
        
        if v in s:
            break
        else:
            s.add(a[i][idx:])
            count += 1

    if len(s) == n:
        break

if len(a[0]) == 1:
    print(1)
else:
    print(len(list(s)[0]))