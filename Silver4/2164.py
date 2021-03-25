from collections import deque
    # 1. 한장 위에 버리기
    # 2. 제일 밑으로 이동

def main():
    c = int(input())
    q = deque([])

    for i in range (c, 0, -1):
        q.append(i)

    
    while(len(q) != 1):
        q.pop()

        #제일 위에 있는거 밑으로 이동
        a = q.pop()
        q.appendleft(a)

    print(q[0])

main()