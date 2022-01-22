from collections import deque

bracket = input()
q = deque()

bracket = list(bracket)
for i in range (len(bracket)):
    q.append(bracket[i])

print(q)

# () 썅
for i in range (len(bracket)):
    # 썅인지 아닌지
    