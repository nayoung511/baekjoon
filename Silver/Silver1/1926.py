"""
1. 아이디어 
- 2중 for => 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수  +1, 최대값을 갱신

2. 시간복잡도
- BFS: O(V+E)
- V = m * n / 500 * 500
- E = V * 4 / 4 * 500 * 500
- V+E: 5 * 25000 = 100만 < 2억

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)

"""

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
mapA = [list(map(int, input().split())) for _ in range (n)]
chk = [[False] * (m) for _ in range (n)]

# E, N, W, S
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        # 동서남북
        for k in range (4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<= ny < n and 0 <= nx < m:
                if mapA[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))

    return rs

cnt = 0
maxV = 0
for j in range (n):
    for i in range (m):
        if mapA[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수 +1 
            cnt += 1
            # BFS > 그림 크기 구하기
            maxV = max(maxV, bfs(j, i))
            # 최댓값 갱신

print(cnt)
print(maxV)