from sys import stdin

n = int(input())
num = list(map(int, stdin.readline().split()))

def consecutiveSumR2L(num, dpR2L):
    n = len(num)
    dpR2L[n-1] = num[n-1]

    for i in range (n-2, -1, -1):
        dpR2L[i] = max(dpR2L[i+1] + num[i], num[i])


def consecutiveSumL2R(num, dpL2R):
    dpL2R[0] = num[0]
    r = dpL2R[0]

    for i in range (1, len(num)):
        dpL2R[i] = max(dpL2R[i-1] + num[i], num[i])
        r = max(r, dpL2R[i])

    
    return r

dpL2R = [0 for i in range (n)]
r = consecutiveSumL2R(num, dpL2R)

dpR2L = [0 for i in range (n)]
consecutiveSumR2L(num, dpR2L)

for idx in range (n):
    if idx > 0:
        r = max(r, dpL2R[idx-1])

    if idx < n-1:
        r = max(r, dpR2L[idx+1])

    if (idx > 0 and idx < n-1):
        r = max(r, dpL2R[idx-1] + dpR2L[idx+1])

print(r)
