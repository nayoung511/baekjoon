from collections import deque
N = int(input())

def countIncreasing(num):
    # 몇 개나 증가하는지 확인
    q = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    arr = [i for i in range (1, 10)]
    total = 9
    if num <= 9 : 
        print(q[num])
        exit(0)
    
    while q:
        c = q.popleft()
        for i in range(0, 10):
            if int(c[-1]) <= i:
                if int(c[-1]) != 0 and i != 0:

                    q.append(c+str(i))
                    arr.append(c+str(i))

                    if int(c+str(i)) >= num: 
                        return len(arr)

def increasing(k):
    flag = True
    arr = list(map(int, str(k)))
    for i in range (len(arr)-1):
        if arr[i] > arr[i+1]:
            flag = False
            break

    if flag == False:
        return -1
    else:
        return 0

for i in range (N):
    num = int(input())

    # 먼저 이 수가 증가하는 수인지 확인
    if increasing(num) == -1:
        print(-1)

    else:
        print(countIncreasing(num))