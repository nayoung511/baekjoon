def nextTour(a, b, flag):
    if len(b) % 2 == 0:
        next = [0] * (len(b) // 2)
    else:
        next = [0] * (len(b) // 2 + 1)
    idx = 0

    for i in range (len(next)):
        if a[idx] == k and a[idx+1] == l: # e.g) 1, 2
            flag = True
            break

        else:
            #print("here?", a[idx:idx+2])
            if k in a[idx:idx+2]:
                next[i] = k
            elif l in a[idx:idx+2]:
                next[i] = l
            else:
                #print(a[idx], a[idx+1])
                next[i] = max(a[idx], a[idx+1])
            idx+=2

        #print(next)
    return next, flag


n, k, l = list(map(int, input().split()))

check = [False] * n
a = [i+1 for i in range (n)]
next = [0] * n
count = 0
flag = False

if k == 1 and l == 2:
    count = 1
else:
    while (flag == False and count <5):
        next, flag = nextTour(a, next, flag)
        count += 1
        #print("next", next, flag)
        a = next
print(count)

