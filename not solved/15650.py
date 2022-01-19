n, m = input().split()
n = int(n)
m = int(m)

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
if m == 1:
    for i in range (1, n+1):
        print(i)

if n == m:
    for i in range (1, n+1):
        print(i, sep =' ')

else:

