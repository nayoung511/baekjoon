from sys import stdin
def sumNum(a):
    num = 0
    for char in a:
        if char.isdigit():
            num+= int(char)

    return num

def swap(a, b):
    temp = a
    a = b
    b = temp
    
n = int(input())
s = []
ans = []
for _ in range (n):
    serial = stdin.readline().rstrip()
    s.append(serial)

s.sort(key=len)
print(s)

#서로 길이가 같다면, A의 모든 자리수의 합, B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저
idx = 0
for i in range (idx+1, n-1):
    print(len(s[idx]), len(s[i]))
    if len(s[idx]) == len(s[i]):
        print("num comp", sumNum(s[idx]), sumNum(s[i]))
        if sumNum(s[idx]) > sumNum(s[i]):
            swap(s[idx], s[i])
        elif sumNum (s[idx]) == sumNum(s[idx]):
            print("hi")

    print(s)
    


