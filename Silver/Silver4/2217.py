import sys
input = sys.stdin.readline

n = int(input())
rope = []
for i in range (n):
    rope.append(int(input()))

rope.sort(reverse = True)

netWeight = [rope[i] * (i+1) for i in range (n)]
print(max(netWeight))

