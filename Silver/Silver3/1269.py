from sys import stdin
a, b = input().split()
a = int(a)
b = int(b)

a_set = set()
a_ele = stdin.readline().split()

for item in a_ele:
    a_set.add(item)

b_set = set()
b_ele = stdin.readline().split()

for item in b_ele:
    b_set.add(item)

# a-b
c = a_set-b_set

# b-a
d = b_set-a_set

print(len(c)+len(d))