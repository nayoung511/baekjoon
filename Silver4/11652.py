from collections import Counter

n = int(input())
a = []

for i in range (n):
    m = int(input())
    a.append(m)
a.sort()
b = Counter(a).most_common()

for i in range (len(b)):
    b[i] = list(b[i])
print(b[0][0])
