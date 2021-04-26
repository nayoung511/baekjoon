a, p = map(str, input().split())

d = [0] * 1000000
d[0] = list(a)
sequence = [0]
sequence[0] = int(a)
idx = 0

while (True):
    value = 0
    for i in range (len(d[idx])):
        value += pow(int(d[idx][i]), int(p))
    if value in sequence:
        del sequence[sequence.index(value):idx+1]
        break
    else:
        d[idx+1] = list(str(value))
        sequence.append(value)
        idx= idx+1
print(len(sequence))