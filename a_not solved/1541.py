from sys import stdin

s = list(stdin.readline().rstrip())
print(s)
symbol = []
num=[]
a = ''
for i in range (len(s)):
    if s[i].isdigit() == False:
        symbol.append(s[i])
        num.append(int(a))
        a = ''
    else:
        a = a+s[i]

num.append(int(a))
print(symbol)
print(num)

# 처음이 - 일 때 
sum = 0
for i in range (len(symbol)):
    if symbol[i] == '-':
        sum += max()
    if symbol[i] == '+':
        sum += 
