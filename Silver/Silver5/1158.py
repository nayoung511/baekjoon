"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmg:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head =="":
            self.next = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def deleteHead(self):
        temp = self.head.data
        self.head = self.head.next

        return temp
        
    def delete(self, data):
        node = self.head
        while node.next:
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                del temp
            else:
                node = node.next

    def traverse(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

def main():
    n, k = input().split()
    n = int(n)
    k = int(k)
    ans = ['<']

    q = NodeMgmg(1)

    for i in range (2, n+1):
        q.add(i)

    for i in range(n-1):
        for j in range(k):
            if j != k-1:
                a = q.deleteHead()
                q.add(a)
            elif j == k-1:
                a = q.deleteHead()
                ans.append(a)
                ans.append(', ')

    a = q.deleteHead()
    ans.append(a)

    ans.insert(len(ans), '>')
    ans = ''.join(map(str, ans))


    print(ans)
    
main()

"""

from collections import deque

n, k = input().split()
n = int(n)
k = int(k)
q = deque([])
ans = ['<']

for i in range (1, n+1):
    q.append(i)

while len(q) > 1:
    for i in range(k-1):
        a = q.popleft()
        q.append(a)
    a = q.popleft()
    ans.append(a)
    ans.append(', ')

ans.append(q.popleft())
ans.append('>')

ans = ''.join(map(str, ans))
print(ans)


