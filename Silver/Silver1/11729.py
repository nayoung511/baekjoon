import sys
input = sys.stdin.readline

n = int(input()) # 원판 수
ans = []
def hanoi(disk, from_, to):
    if disk == 1:
        print(from_, to)
    else:
        hanoi(disk-1, from_, 6-from_-to)
        print(from_, to)
        hanoi(disk-1, 6-from_-to, to)

print(2**n - 1)
hanoi(n, 1, 3)