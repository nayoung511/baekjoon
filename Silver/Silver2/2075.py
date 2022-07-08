import sys
input = sys.stdin.readline

n = int(input())
idx = [[1 for i in range (n)] for i in range (n)]
matrix = []
for i in range (n):
    a = list(map(int, input().split()))
    a.sort(reversed)
    matrix.append(a)

for i in range (n):
    print(matrix[i])







row, col = n-1, n-1
num = 2
for i in range (n):
    if row >= 0 and col >= 0:
        # 옆과 위 비교
        # 위의 값이 더 크다면
        if matrix[row-1][col] > matrix[row][col-1]:
            # 위로 이동
            idx[row-1][col] = num
            idx[row][col-1] = num + 1
            row = row-1
        else:
            idx[row][col-1] = num
            idx[row-1][col] = num + 1
            col = col-1

        num += 2
        print(matrix[row][col])

for i in range (n):
    print(idx[i])

print(idx)

