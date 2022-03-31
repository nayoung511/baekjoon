n, l = map(int, input().split())
tape = list(map(int, input().split()))
trange = tape.copy()

for i in range (len(tape)):
    trange[i] = tape[i] - 0.5 + l
count = 0

print(trange)
check = [0] * (int(max(trange)))
print(check)

tape.sort()
tape.reverse()
max = tape[0]
for i in range (n):
    print(trange[i], max)
    if trange[i] < max:
        count+=1
        max = tape[i]


print(count)