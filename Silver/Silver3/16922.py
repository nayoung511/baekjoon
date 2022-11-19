# 중복조합 사용
from itertools import combinations_with_replacement
roman = [1, 5, 10, 50]

n = int(input())
unique = set()
for temp in combinations_with_replacement(roman, n):
    unique.add(sum(temp))

print(len(unique))

# recursive - dfs

n = int(input())
roman = [1, 5, 10, 50]
visited = [False for i in range (50 * 20 + 1)]
count = 0

def dfs(depth, index, total):
    global count
    if depth == n:
        if not visited[total]:
            visited[total] = True
            count += 1
        return

    for i in range (index, 4):
        dfs(depth+1, i, total + roman[i])

dfs(0,0,0)
print(count)

