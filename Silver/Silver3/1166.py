# n개의 박스 - 크기 a^3
# a의 최댓값

n, l, w, h = map(int, input().split())
start, end = 0, max(l, w, h)

for _ in range (100):
    mid = (end + start) / 2
    if (l//mid) * (w//mid) * (h//mid) >= n:
        start = mid
    else:
        end = mid

print(end)


