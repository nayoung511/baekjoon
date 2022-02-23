import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

# OI를 체크
#I = 'OI'
count = 0
io=0
i = 0
while i < m-1:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        io+= 1
    # n 횟수만큼 체크 
        if io == n:
            count+=1
            io -= 1
    else:
        io = 0
    if io != 0:
        i += 2
    else:
        i+=1
    #print(i, count, io)
            

print(count)

"""
# 50점
count = 0
# set IOI
I = 'I'
for _ in range (n):
    I += 'OI'

for j in range (m):
    if s[j] == 'I':
        if (s[j:j+len(I)]) == I:
            count+=1

print(count)

"""