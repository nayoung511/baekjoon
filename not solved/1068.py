import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
delete = int(input())
count = 0
def dfs(start, count):
    count += 1
    visited[start] = True

    for y in num[start]:
        if visited[y] == False:
            dfs(y, count)

    return count

            

visited = [False for _ in range (n+1)]


count = dfs(num[delete], count)
print(len(num) - count)

