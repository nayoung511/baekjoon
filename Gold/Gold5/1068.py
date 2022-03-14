import sys
input = sys.stdin.readline

def dfs(start):
    num[start] = -2

    for i in range (len(num)):
        if start == num[i]:
            dfs(i)

n = int(input())
num = list(map(int, input().split()))
delete = int(input())
count = 0

dfs(delete)
for i in range (len(num)):
    if num[i] != -2 and i not in num:
        count += 1
print(count)

