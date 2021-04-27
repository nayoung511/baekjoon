n, l = map(int, input().split())

#num = [i+1 for i in range (n)]
#print(num)

flag = True
sumn = 0
s = n - 1
e = n - 2

count = 0
while (sumn != n):
    num = [i+1 for i in range (n-2, n)]
    sumn = 0
    
    print(num[s:e+1])
    sumn += sum(num[s:e+1])
    print(num[s:e+1], sumn)

    if sumn == n:
        break
    elif sumn < n:
        #print("he", s,  num[0])
        if s == num[0]-1:
           flag = False
           break
        else:
            s = s - 1
        #print(s)
    else:
        s = s - 1
        e = e - 1

        if e == 2:
            flag = False
            break

    count +=1
#print(num[s:e])

if (len(num[s:e]) > 100 or flag == False):
    print(-1)
else:
    for i in num[s:e]:
        print(i, end=" ")
    