import sys
input = sys.stdin.readline


def visit(depth, idx):
    if depth == 6:
        print(*num)
        return

    for i in range (idx, a[0]):
        num.append(arr[i])
        visit(depth+1, i+1)
        num.pop()
        

while True:
    a = list(map(int, input().split()))
    arr = a[1:]
    num = []
    visit(0, 0)
    if a[0] == 0:
        exit()
    print()