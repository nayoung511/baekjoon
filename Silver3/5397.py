from collections import deque
#백스페이스 -
#커서 이동 < >

n = int(input())
a = []
flag = True
for _ in range (n):
    command = list(input())
    q = deque()
    idx = 0
    for i in range (len(command)):
        if command[i] == "<":
            flag = True
            q.rotate(-1)
        if command[i] == ">":
            flag = False
            q.rotate(1)
        if command[i] == "-":
            if len(q) > 0:
                q.pop()
        elif command[i].isalpha() or command[i].isdigit():
            if flag == False:
                q.append(command[i])
            else:
                q.appendleft(command[i])
        print(command[i],q)
        
    q = list(q)
    ans = ''.join(map(str, q))
    a.append(ans)

for i in a:
    print(i)

