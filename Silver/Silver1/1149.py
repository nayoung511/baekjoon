import sys
input = sys.stdin.readline

n = int(input())
arr = []
r, g, b = [int(x) for x in input().split()] # 값이 하나만 있을 경우
arr.append((r, g, b))

for _ in range (1, n):
    r, g, b = [int(x) for x in input().split()]
    pR, pG, pB = arr[-1] # 이전 값
    # 현재 색 값 + 다음에 올 수 있는 최소 값
    R = r + min(pG, pB)
    G = g + min(pB, pR)
    B = b + min(pR, pG)
    arr.append((R, G, B))

fR, fG, fB = arr[-1]
print(min(fR, fG, fB))
