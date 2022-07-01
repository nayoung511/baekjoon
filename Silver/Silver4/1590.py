import sys
input = sys.stdin.readline

n, t = map(int, input().split())
ans = []
# 버스의 시작 시간, 간격, 대수
for _ in range (n):
    start_time, gap, num = map(int, input().split())

    # 시간 간격 계산
    schedule = [start_time + (gap * i) for i in range (num)]
    # 배차 끝시간이 범위 안인지 확인
    if schedule[-1] < t:
        continue
    start, end = 0, num-1
    count = 0
    # 이분 탐색
    while end >= start:
        mid = (start + end) // 2

        if schedule[mid] >= t:
            count = mid
            end = mid -1
        else:
            start = mid + 1

    ans.append(schedule[count] - t)

print(min(ans) if ans else -1)



    


