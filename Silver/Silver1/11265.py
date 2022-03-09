import sys
input = sys.stdin.readline

# 파이장 크기, 손님
n, m = map(int, input().split())
num = [0 for _ in range (n)]
party = [0 for _ in range (m)]
for i in range (n):
    num[i] = list(map(int, input().split()))

for i in range (m):
    # 손님이 위치한 파티장, 다음 파티장, 다음 파티가 열리는데 걸리는 시간
    party[i] = list(map(int, input().split()))


# 거쳐가기
for k in range (n):
    # 출발 
    for i in range (n):
        # 도착 
        for j in range (n):
            if (num[i][k] + num[k][j] < num[i][j]):
                num[i][j] = num[i][k] + num[k][j]


for i in range (m):
    # i -> j 에서 가는 시간이 num[i][j]보다 오래걸리면 stay here
    # stay here = 1
    # enjoy other party = 0
    if num[party[i][0] - 1][party[i][1] - 1] > party[i][2]:
        print("Stay here")
    else:
        print("Enjoy other party")

