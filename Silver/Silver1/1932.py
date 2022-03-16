import sys
input = sys.stdin.readline

n = int(input())
pyra = []
for _ in range (n):
    pyra.append(list(map(int, input().split())))

k = 2
for i in range (1, n):
    for j in range (k):
        if j == 0:
            pyra[i][j] = pyra[i][j] + pyra[i-1][j]

        elif i == j:
            pyra[i][j] = pyra[i][j] + pyra[i-1][j-1]
        else:
            pyra[i][j] = max(pyra[i-1][j], pyra[i-1][j-1]) + pyra[i][j]

    k += 1
print(max(pyra[n-1]))
