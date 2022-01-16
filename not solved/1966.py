from collections import deque
# Test case number
nOT = int(input())
q = deque()
ans = []

for _ in range (nOT):
    # n = 문서의 갯수
    # m = 몇 번째 관심
    n, m = map(int, input().split())
    priority = deque((map(int, input().split())))

    print(priority)

    order = 0
    pSort = list(priority.copy())
    pSort.sort()
    pSort.reverse()

    q.append(pSort)
    print(q)

    #제일 높은 우선 순위
    maxP = pSort[0]

    print(pSort)
    if n == 1:
        ans.append('1')

    else:
        for i in range (n, 0, -1):
            # 제일 높은 우선 순위가 아니라면
            if priority[i] != maxP:
                # 맨 뒤에 배치
                q.append(priority[i])
            
                


    



print(priority[-m])


"""
예제 입력 1 
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

예제 출력 1 
1
2
5
"""