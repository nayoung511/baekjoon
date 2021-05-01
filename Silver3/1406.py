s = input()

s = list(s)
num = int(input())

idx = len(s)
for i in range (num):
    inst = input()
    inst = list(inst)

    if inst[0] == 'L':
        if idx > 0:
            idx = idx - 1

    if inst[0] == 'D':
        if idx < len(s) - 1:
            idx = idx + 1

    if inst[0] == 'B':
        if idx > 0:
            del s[idx-1]

    if inst[0] == 'P':
        s.insert(idx, inst[-1])

print(s)