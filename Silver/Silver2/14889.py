import sys
input = sys.stdin.readline

n = int(input())
team = [list(map(int, input().split())) for _ in range (n)]
visited = []
start = []
link = []
def dfs():
