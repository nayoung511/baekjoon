import sys
input = sys.stdin.readline

t = int(input())
for _ in range (t):
    n = int(input()) # 동전의 가지수
    coin = list(map(int, input().split()))
    goal = int(input())

    


'''
최소 coin[-1] ~ coin[0]

1 2
10

최소 10/2= 5 ~ 10 / 1 = 10
5~10가지의 경우
sol[0] = 5
sol[4] = 10

   1   2
0    0
1    1
2    2
3
4



'''