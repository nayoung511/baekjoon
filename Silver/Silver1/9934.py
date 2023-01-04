import sys
input = sys.stdin.readline

K = int(input())
buildings = list(map(int, input().split()))
tree = [[] for _ in range (K)]

def makeTree(building, x):
    print("current", x, building)
    # mid = 루트
    mid = len(building)//2
    tree[x].append(building[mid])

    if len(building) == 1:
        return

    makeTree(building[:mid], x+1) # 왼쪽
    makeTree(building[mid+1:], x+1) # 오른쪽

makeTree(buildings, 0)
for i in range (K):
    print(*tree[i])