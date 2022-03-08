import sys
input = sys.stdin.readline
INF = 100000

# 교차로의 수
n = int(input())
cycle = False
# 배열 초기화
cross = [[INF for _ in range (n)] for _ in range (n)]

for i in range (n-1):
    m = int(input()) #i번 교차로와 연결된 교차로의 수
    c = list(map(int, input().split())) #i번째에서 갈 수 있는 교차로의 번호
    for j in c:
        cross[i][j-1] = 1

# 내가 i -> j로 갔는데 or i -> k -> j
# j -> i로 갈 수 있으면 or j -> k -> i

# 거쳐가는 노드
for k in range (n):
    # 시작 노드 
    for i in range (n):
        # 도착 노드
        for j in range (n):
            if (cross[i][j] > cross[i][k] + cross[k][j]):
                cross[i][j] = cross[i][k] + cross[k][j]

for i in range (n):
    for j in range (n):
        # 나와 연결되어 있고, 
        if 0<cross[0][j]<INF:
            # 얘네들끼리 cycle이 있다면 
            if (0<cross[i][j]<INF and 0<cross[j][i]<INF): 
                cycle = True
                break

if cycle == True:
    print ("CYCLE")
else:
    print("NO CYCLE")