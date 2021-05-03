from collections import deque

n, m = input().split()
n = int(n)
m = int(m)

val = list(map(int, input().split()))

q = deque(i for i in range (1, n+1))

idx = 1
count = 0
i = 0

while(count != m):
    a = q.popleft()
    if val[i] == a:
        i = i + 1
        count += 1

    else:
        if (abs(val[i] - a) > abs(len(q) - val[i])):
            q.rotate(-(abs(val[i]-a) + 1))
            
        else:
            q.rotate(len(q) - val[i] + 1)
        
        print(q)

print(count)


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