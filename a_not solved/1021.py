from collections import deque

n, m = input().split()
n = int(n)
m = int(m)

val = list(map(int, input().split()))
val = deque(val)

q = deque(i for i in range (1, n+1))

count = 0



for i in range (10):
    left = q.popleft()
    q.appendleft(left)

    right = q.pop()
    q.append(right)

    first = val.popleft()
    val.appendleft(first)

    print("first", first, "left", left, "right", right)
    print(q)
    if first == left:
        q.popleft()
        
        val.popleft()
        

    else:
        if first - left < right - first:
            a = q.popleft()
            q.append(a)
            count+=1
            
        else:
            a = q.pop()
            q.appendleft(a)
            count+=1

        
    print(q, "\n")


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



