import sys
input = sys.stdin.readline
INF = 1000000

# 배열 초기화
n, m = map(int, input().split())
friend = [[0 for i in range (n)] for j in range (n)]
val = [0 for i in range (n)]

for i in range (m):
    a, b = map(int, input().split())
    friend[a-1][b-1] = 1
    friend[b-1][a-1] = 1


for i in range (n):
    for j in range (n):
        if i != j:
            if friend[i][j] == 0:
                # 친구가 없는 상태라면
                # 무한대 값으로 설정
                friend[i][j] = INF

#  k = 거쳐가는 노드 
for k in range (n):
    # i = 출발 노드
    for i in range (n):
        # j = 도착 노드
        for j in range (n):
            if (friend[i][k] + friend[k][j] < friend[i][j]):
                friend[i][j] = friend[i][k] + friend[k][j]


minn = sum(friend[0])
idx = 0
for i in range (n):
    if sum(friend[i]) < minn:
        minn = sum(friend[i])
        idx = i

print(idx+1)
