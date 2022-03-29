import sys
input = sys.stdin.readline

# 물품의 수, 최대 무게
n, k = map(int, input().split())

# 물건의 무게를 track
table = [0] * (k+1)

for _ in range (n):
    # 물건의 무게, 물건의 가치
    w, v = [int(x) for x in input().split()]
    if w > k:
        continue
    for j in range (k, 0, -1):
        if j + w <= k and table[j] != 0:
            table[j+w] = max(table[j+w], table[j]+v)
    table[w] = max(table[w], v)

print(max(table))

