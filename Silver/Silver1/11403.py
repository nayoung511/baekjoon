import sys
input = sys.stdin.readline

# i -> j로 가는 경로가 있는지
n = int(input())
num = [list(map(int, input().split())) for _ in range (n)]

# 거쳐가는 노드
for k in range (n):
    # 출발노드
    for i in range (n):
        # 도착노드
        for j in range (n):
            if (num[i][k] ==1 and num[k][j] == 1):
                num[i][j] = 1

for i in range (n):
    for j in range (n):
        print(num[i][j], end=' ')
    print()