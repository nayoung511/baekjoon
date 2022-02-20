# 집합
import sys
input = sys.stdin.readline

m = int(input()) # 3,000,000

# 공집합 선언
# s=bin(0) --> 문자열이 된다
s = 0
for _ in range (m):
    ist = list(map(str, input().split()))
   #print(ist)

    if ist[0] == 'add':
        s |= (1 << int(ist[1]))

    if ist[0] == 'check':
        print(1 if s & (1 << int(ist[1])) !=0 else 0)

    if ist[0] == 'remove':
        s &= ~(1 << int(ist[1]))

    if ist[0] == 'toggle':
        # x가 있으면 x를 제거, 없으면 추가 XOR
        s ^= (1 << int(ist[1]))
        # if s & (1 << int(ist[1])):
        #     s &= ~(1 << ist[1])
        # else:
        #     s |= (1 << ist[1])
    
    if ist[0] == 'all':
        s = (1 << 21) -1;

    if ist[0] == 'empty':
        s = 0


# 원소 추가