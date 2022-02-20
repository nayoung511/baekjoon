from collections import deque
from sys import stdin

def peek(q):
    a = q.pop()
    q.append(a)

    return a

def main():
    c = int(input())
    

    for i in range (c):
        q = deque([])
        inp = stdin.readline()

        for j in range(len(inp)):            
            if len(q) ==0:
                if inp[j] == "(":
                    q.append(inp[j])
                if inp[j] ==")":
                    q.append(")")

            elif len(q) != 0:
                if inp[j] == "(":
                    q.append(inp[j])

                if inp[j] == ")":
                    # ( 가 들어가 있으면 Pop
                    if peek(q) == "(":
                        q.pop()
                    else:
                        q.append(inp[j])
        
        if len(q) != 0:
            print("NO")
        else:
            print("YES")

main()