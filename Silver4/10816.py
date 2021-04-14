from sys import stdin
from collections import Counter

n = int(input())
a = list(map(int, stdin.readline().split()))

m = int(input())
b = list(map(int, stdin.readline().split()))

c = Counter(a)

for i in b:
    print(c[i], end=" ")
