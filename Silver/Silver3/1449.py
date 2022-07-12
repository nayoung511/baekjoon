import sys
input = sys.stdin.readline

n, l = map(int, input().split())
tape = list(map(int, input().split()))

tape.sort()

start = tape[0]
end = tape[0] + l

tapeNum = 1
for i in range (n):
    if start <= tape[i] < end:
        continue
    else:
        # 새로운 시작점으로
        start = tape[i]
        end = tape[i] + l
        tapeNum += 1
print(tapeNum)