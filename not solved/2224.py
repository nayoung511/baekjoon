import sys
input = sys.stdin.readline

n = int(input())

p = [" " for i in range (n)]
a = []
for i in range (n):
    temp = list(map(str, input().split(sep=" => ")))
    temp[-1] = temp[-1].strip()
    p[i] = temp
    for i in p[i]:
        if i not in a:
            a.append(i)


a.sort()
print(a)
print(p)

prop = [[0 for i in range (len(a))] for i in range (len(a))]
#print(prop)
pos = 0
t = [[0 for i in range (len(a))] for i in range (len(a))] 
left = 0
right = 0
val = 0

for j in p:
    for i in range (len(a)):
        if j[0] == a[i]:
            left = i

    for i in range (len(a)):
        if j[1] == a[i]:
            right = i
            val = a[i]

    prop[left][right] = val
    t[left][right] = 1

for i in range (len(a)):
    t[i][i] = -1

print(prop)

value = 0
# 출발
for i in range (len(a)):
    # 도착
    for j in range (len(a)):
        if prop[i][j] != 0:
        # 도착이 뭔지 확인
            check = a.index(prop[i][j])
            #print(check)
            for k in range (len(a)):
                if prop[check][k] != 0:
                    ch2 = a.index(prop[check][k])
                    #print(prop[check][k])
                    prop[i][ch2] = prop[check][k]

print(prop)
count = 0
for i in range (len(a)):
    for j in range (len(a)):
        if prop[i][j] != 0:
            count+=1
print(count)

for i in range (len(a)):
    for j in range (len(a)):
        if prop[i][j] != 0:
            print(a[i], "=>", prop[i][j])