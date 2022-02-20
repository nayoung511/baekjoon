from sys import stdin
from collections import deque

d = deque()
rev = deque()

s = list(stdin.readline().rstrip())

for i in range (len(s)):
    d.append(s[i])
count = 0

while len(d) > 0:
    # tag 인지 확인 
    a = d.popleft()
    d.appendleft(a)

    if a == '<':
        b = d.popleft()
        d.appendleft(b)

        while b != '>':
            print(b, end='')
            d.popleft()
            #print("d", d)
            b = d.popleft()
            d.appendleft(b)
        
        b = d.popleft()
        d.appendleft(b)

        print(b, end='')
        d.popleft()

    elif a == ' ':
        print(a, end='')
        d.popleft()

    else:
        b = d.popleft()
        d.appendleft(b)

        # space가 아닐 때까지 
        while b != ' ' and  b != '<' and len(d) > 0:
            rev.appendleft(b)
            d.popleft()
            #print("d", d)
            if len(d) > 0:
                b = d.popleft()
                d.appendleft(b)
                #print(d)

        while len(rev) != 0:
            b = rev.popleft()
            rev.append(b)

            print(b, end='')

            rev.pop()

#print(d, rev)



