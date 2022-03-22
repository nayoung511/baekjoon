import sys
input = sys.stdin.readline

first = list(map(str, input().rstrip()))
second = list(map(str, input().rstrip()))

matrix = [[0 for i in range (len(second)+1)] for j in range (len(first)+1)]

for i in range (1, len(first)+1):
    for j in range (1, len(second)+1):
        if first[i-1] == second[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

#   matrix
#   second
#f
#i
#r
#s
#t

for i in range(len(first)+1):
    for j in range (len(second)+1):
        print(matrix[i][j], end='')

    print()

print(matrix[-1][-1])