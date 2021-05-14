from collections import deque

n, m = input().split()
n = int(n)
m = int(m)

val = list(map(int, input().split()))

q = deque(i for i in range (1, n+1))

print(q)
idx = 1
count = 0
i = 0
rotate = 0

while(count != m and rotate < 15):
    a = q[0]   #most front element in the queue
    print("front", a, "val", val[i])
    if val[i] == a: #if a is same as target,
        q.popleft()
        i = i + 1
        count += 1
<<<<<<< HEAD
#음수 = 왼쪽 
#양수 = 오른쪽 
    else:
        print(val[i] - a, len(q)-val[i])
        if (abs(val[i] - a) < abs(len(q)-val[i])):
            q.rotate(-abs(val[i]-a))
            rotate += abs(val[i]-a)
            
        else:
            q.rotate(len(q)-val[i] + 1)
            rotate += len(q) - val[i] + 1
        
    count += 0.2
    print(q, rotate)
print(rotate)
=======

    else:
        if (abs(val[i] - a) > abs(len(q) - val[i])):
            q.rotate(-(abs(val[i]-a) + 1))
            
        else:
            q.rotate(len(q) - val[i] + 1)
        
        print(q)

print(count)
>>>>>>> 9f631d46f6ceda04bff2bcbf907145f1992fd23e


"""
1. 첫번째 원소 pop
2. 왼쪽으로 이동 a1 pop
3. 오른쪽으로 이동 ak pop


1 2 3 4 5 6 7 8 9 10

2 3 4 5 6 7 8 9 10 1   / 1

1 3 4 5 6 7 8 9 10     / 2
10 1 3 4 5 6 7 8 9      / 3
9 10 1 3 4 5 6 7 8       / 4
10 1 3 4 5 6 7 8       / 4

8 10 1 3 4 5 6 7        / 5

7 8 10 1 3 4 5 6       / 6

6 7 8 10 1 3 4 5       / 7

5 6 7 8 10 1 3 4      / 8

"""



