import sys
input = sys.stdin.readline
n = int(input())
maxcount = 0
count = [0]
for i in range (n):
    count[0]=0
    inst = list(input().rstrip())
    for j in range (len(inst)):
        if inst[j] == 'f':
            if j+2 < len(inst):
                a = inst[j]+inst[j+1]+inst[j+2]
                if a == 'for':
                #if ''.join(inst[j:3]) == 'for':
                    count[0]+=1

        if inst[j] == 'w':
            if j+4 < len(inst):
                a = inst[j]+inst[j+1]+inst[j+2]+inst[j+3]+inst[j+4]
                if a == 'while':
                    count[0]+=1

    if count[0] > maxcount:
        maxcount = count[0]
    

print(maxcount)