n = int(input())
arr = [-1 ]
# 0: 0번째

def decreasing(k):
    if len(arr) == n+1:
        return

    for s in range (10000000):
        flag = False
        num = list(map(int, str(s)))

        for i in range (len(num)-1):
            if num[i] <= num[i+1]:
                flag = True
                break

        if flag == False:
            arr.append(s)

        if len(arr) == n+1:
            return

decreasing(0)
print(len(arr))
if len(arr) < n:
    print(-1)
else:
    print(arr[n])
# 0 1 2 3 4 5 6 7 8 9 (9)
# 10 20 21 30 31 32 40 41 42 
