from collections import deque

q = deque([])
n = int(input())
a = []
sign = []
out = []

m = 1
for i in range (n):
    c = int(input())
    a.append(c)

count = 0
idx = 0
while count < n:
    if m < a[idx]:
        for i in range (a[idx] - m + 1):
            q.append(m)
            sign.append('+')
            m = m + 1

            print(q)

        q.append(m)
        sign.append('+')

        b = q.pop()
        out.append(b)
        sign.append('-')
        count = count + 1

    else:
        for i in range (m - a[idx]):
            b = q.pop()
            out.append(b)
            sign.append('-')
            count = count + 1

    idx = idx + 1


for item in sign:
    print(item)
        



