import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

tree = []
count = 0
while True:
    try:
        tree.append(int(input()))
    except:
        break

def binaryTree(start, end):
    if start > end:
        return
    else:
        mid = end + 1
        for i in range (start + 1, end + 1):
            if tree[start] < tree[i]:
                mid = i
                break
            
        binaryTree(start + 1, mid - 1)
        binaryTree(mid, end)
        print(tree[start])

binaryTree(0, len(tree)-1)
    