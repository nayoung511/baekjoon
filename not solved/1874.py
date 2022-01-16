from collections import deque
from sys import stdin
n = int(input())

# num 넣을 리스트
a = []

# 정답 넣을 리스트
ans = []

#queue
q = deque()

# pop 완료된 리스트 // a 와 같아야 함
check = []

for i in range (n):
    inp = int(stdin.readline())
    a.append(inp)


start = 0
val = 1
flag = True
while len(check) != len(a):

# if the last element in the list equls to the element in a
    if len(q) != 0:
        
        # 큐의 첫 원소를 확인하고 다시 넣어줌
        first = q.pop()
        q.append(first)

        if first == a[start]: 
            #print(start, first, a[start])
            #print("-")
            ans.append("-")
            #print("gonna append", first)
            check.append(first)
            q.pop()
            #print(q, "check:   ", check)
            start += 1

        else:
            if val >= a[start] + 1:
                flag = False
                #print("NO")
                break
            for i in range (val, a[start]+1):
                #print(val, a[start], i, start)
                q.append(i)
                #print("+", q)
                ans.append("+")
                val = a[start] +1
            
        
    # 빈 큐일 때 필요한 횟수만큼 집어 넣는다
    if len(q) == 0 and len(check) != len(a):
        for i in range (val, a[start]+1):
            #print(val, a[start], i, start)
            q.append(i)
            #print("+", q)
            ans.append("+")
        val = a[start] + 1
 
    
if flag == True:
    print(*ans, sep="\n")
else:
    print("NO")
