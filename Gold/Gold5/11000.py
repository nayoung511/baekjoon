import sys
from collections import deque
input = sys.stdin.readline

def cal(lecture, idx):
    lecs = []
    # 다음 수업 시작 시간
    next_class = lecture[idx][1]
    lecs.append(idx)

    for i in range (idx+1, len(lecture)):
        # 남아있는 수업 중에 이 시간이나 이 시간 후에 
        if lecture[i][0] >= next_class:
            next_class = lecture[i][1]

            lecs.append(i)
            print(next_class)

    return lecs


n = int(input())
lecture = deque([])

idx = 0
min_start = 0
for i in range (n):
    a, b = map(int, input().split())
    if i == 0:
        min_start = a
    min_start = min(min_start, a)
    lecture.append((a, b))

print(min_start)
print(lecture)