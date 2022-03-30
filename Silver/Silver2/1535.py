import sys
input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
table = [[0] * 101 for _  in range (n+1)]

for i in range (1, n+1):
    for j in range (100):
        if j < hp[i-1]:
            table[i][j] = table[i-1][j]

        else:
            table[i][j] = max(table[i-1][j], table[i-1][j-hp[i-1]]+ happy[i-1])

print(table[n][99])