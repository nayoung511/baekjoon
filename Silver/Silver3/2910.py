from sys import stdin
n, m = map(int, input().split())
num = list(map(int, stdin.readline().split()))

d = dict()

for j in range (n):
    if num[j] in d.keys():
        d[num[j]] += 1
    else:
        d[num[j]] = 1

d = sorted(d.items(), key=lambda x: x[1], reverse=True)

ans = [0] * (n)
count = 0

for i in range (len(d)):
    for j in range (d[i][1]):
        ans[count] = d[i][0]
        count+=1


print(*ans)






