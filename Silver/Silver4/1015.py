import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
visited = [-1 for i in range (n)]

start = min(arr)
count = 0
for i in range (max(arr)):
    for j in range (n):
        # 최소값이 어디있는지 찾는다
        if arr[j] == start:
            visited[j] = count
            count += 1
    # 중복 값이 없으면 올림
    start += 1
    # 현재 값 바로 저장

print(*visited)



