import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
max_b=100000

cnt=[0 for i in range (max_b+1)]


def bfs():
    q = deque()
    q.append(n)
    while q:
        ex = q.popleft()
        if ex == k:
            print(cnt[ex])
            break

        for item in (ex-1, ex+1, ex*2):
            if 0 <= item <= max_b and not cnt[item]:
                cnt[item] = cnt[ex] + 1
                q.append(item)


bfs()
