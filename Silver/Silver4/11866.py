from collections import deque
n, k = map(int, input().split())

q=deque([])
ans = []

for i in range (1, n+1):
    q.append(i)

while (len(ans) < n):
    for _ in range (k):
        p = q.popleft()
        q.append(p)
    pf = q.pop()
    ans.append(pf)

print("<", str(ans)[1:-1], ">", sep='')