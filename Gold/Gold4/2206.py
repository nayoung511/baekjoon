import sys
from collections import deque

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 

def bfs():
	q = deque()
	q.append([0, 0, 1])
	visited[0][0][1] = 1
	while len(q) != 0:
		i, j, wall = q.popleft()
		if i == n-1 and j == m-1:
			return visited[i][j][wall]
		for k in range(4):
			a = i+dx[k]
			b = j+dy[k]
			if 0<=a<n and 0<=b<m:
				if wall == 1 and location[a][b] == 1: 
					visited[a][b][0] = visited[i][j][1] + 1
					q.append([a, b, 0])
				elif location[a][b] == 0 and visited[a][b][wall] == 0:
					visited[a][b][wall] = visited[i][j][wall] + 1
					q.append([a, b, wall])
	return -1


n, m = map(int, sys.stdin.readline().split()) 
location = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)] 
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(bfs())
