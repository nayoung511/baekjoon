from sys import stdin
n, m = map(int, input().split())
dictionary = {}
ans=[0] * m
for i in range (n):
    a, b = stdin.readline().split()
    dictionary[a] = b

for i in range (m):
    ans[i] = str(stdin.readline().strip())


for i in range (m):
    if ans[i] in dictionary:
        print(dictionary[ans[i]])