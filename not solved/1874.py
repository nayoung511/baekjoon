from collections import deque
from sys import stdin
n = int(input())
a = []
q = deque()
sign = []
val = []

for i in range (n):
    inp = int(stdin.readline())
    a.append(inp)

start = 1
idx = 0
while len(sign) != len(a):
    if start < a[idx]:
        #차이만큼 push
        for _ in range (a[idx] - start+1):
            q.append(start)
            val.append("+")
            
            if start == a[idx]:
                sign.append(q.pop())
                val.append("-")
                
            start = start + 1

    if start == a[idx] or len(q) == 0:
        q.append(start)
        val.append("+")
        start = start + 1

        sign.append(q.pop())
        val.append("-")

    else:
        for _ in range (start - a[idx]-1):
            sign.append(q.pop())
            val.append("-")

            if len(q) == 0:
                break
    idx = idx + 1

if sign != a:
    print("NO")
else:
    for i in val:
        print(i)
    
