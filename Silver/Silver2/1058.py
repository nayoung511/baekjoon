import sys
input = sys.stdin.readline

n = int(input())
friend = [list(map(str, input().rstrip())) for i in range (n)]

twoFriend = [[0 for i in range (n)] for j in range (n)]

# 거쳐가는 노드 
for i in range (n):
    # 출발 노드 
    for j in range (n):
        # 도착 노드
        for k in range (n):
            #본인은 count 안 함
            if j == k: continue

            # 출발 -> 도착 이 있을 때
            # 출발 -> 거쳐가는 노드 있을 때 && 거쳐가는 -> 도착이 있을 때
            if (friend[j][k] == 'Y' or (friend[j][i] == 'Y' and friend[i][k] == 'Y')):
                twoFriend[j][k] = 1



result = 0
for i in twoFriend:
    result = max(result, sum(i))
            
print(result)