from sys import stdin

n, m = input().split()
n = int(n)
m = int(m)
a = {}
b = []

for i in range(n):
    c = stdin.readline().strip('\n')
    a[c] = i+1
    b.append(c)

for i in range(m):
    c = stdin.readline().strip('\n')
    if c.isdigit():
        print(b[int(c) - 1])
    else:   #알파벳 --> 포켓몬 번호
        print(a[c])


#m개의 줄에 맞춰야하는 문제가 입력으로 들어옴
# 알파벳 --> 포켓몬 번호
# 숫자 --> 포켓몬 번호에 해당하는 문자 출력