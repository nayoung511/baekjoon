import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range (n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='') #root
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right


def inorder(root):
    if root != '.':
        inorder(tree[root][0]) #left
        print(root, end='') #root
        inorder(tree[root][1]) #right

def postorder(root):
    if root != '.':
        postorder(tree[root][0]) #left
        postorder(tree[root][1]) #right
        print(root, end='') #root


# 항상 A가 루트 노드 
preorder('A')
print()
inorder('A')
print()
postorder('A')