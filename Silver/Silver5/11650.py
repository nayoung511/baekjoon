n = int(input())
arr = [] * n
for _ in range (n):
    arr.append(list(map(int, input().split())))

arr.sort()

for i in arr:
    print(" ".join(map(str, i)))