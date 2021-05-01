from sys import stdin

stack1 = list(stdin.readline().rstrip('\n'))
stack2 = []

num = int(input())

for _ in range(num):
    inst = stdin.readline().rstrip('\n')

    if inst[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())

    if inst[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())

    if inst[0] == 'B':
        if stack1:
            stack1.pop()
       
    if inst[0] == 'P':
        stack1.append(inst[-1])

stack2.reverse()
s = ''.join(map(str, (stack1 + stack2)))

print(s)
