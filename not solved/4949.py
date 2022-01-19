from collections import deque
import sys
input = sys.stdin.readline

flag = True
q1 = deque() # [] ()
count_a = 0
count_b = 0
def checkBracket(s):
    for char in s:
        if char == '[' or char == ']' or char == ")" or char =="(":
            q1.append(char)
    
    print("q1", q1)
    # check the length
    if len(q1) % 2 != 0:
        return False

    while(len(q1) > 1):
        left = q1.popleft()
        right = q1.pop()

        q1.appendleft(left)
        q1.append(right)

        print(left, right)

        if left == right:
            return False
        else:
            if left == '[' and right == ']':
                q1.pop()
                q1.popleft()
            if left == '(' and right == ')':
                q1.pop()
                q1.popleft()
            else:
                return False

    if len(q1) == 1:
        return False
    if len(q1) == 0:
        return True


def main():
    while True:
        s = input().rstrip()
        if s == ".":
            break
        if checkBracket(list(s)) == False:
            print("no")
        else:
            print("yes")
    print("yes")


main()